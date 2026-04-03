/** @odoo-module */

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";
import { onMounted, onPatched } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";

// Placeholders are translated via Odoo's _t() — no manual language detection needed.
// Translations live in i18n/ar.po and i18n/fr.po.
const DZ_PLACEHOLDERS = {
    state_id: () => _t("Wilaya"),
    city_id: () => _t("Municipality"),
};

function isAlgeriaSelected(formEl) {
    const countryInput = formEl.querySelector(
        '.o_field_widget[name="country_id"] input'
    );
    if (!countryInput) return false;
    const val = countryInput.value || "";
    return (
        val.includes("Algeria") ||
        val.includes("Algérie") ||
        val.includes("الجزائر") ||
        val.includes("(DZ)")
    );
}

/**
 * Apply DZ placeholders to state_id and city_id fields.
 * Returns true if all fields were found, false if city_id was not yet
 * rendered (caller should retry after enforce_cities re-render).
 */
function applyDzPlaceholders(formEl) {
    const isDZ = isAlgeriaSelected(formEl);
    let allFound = true;

    for (const fieldName of ["state_id", "city_id"]) {
        const input = formEl.querySelector(
            `.o_field_widget[name="${fieldName}"] input`
        );
        if (!input) {
            if (isDZ) allFound = false;
            continue;
        }

        if (isDZ) {
            if (!input.dataset.origPlaceholder) {
                input.dataset.origPlaceholder = input.placeholder;
            }
            input.placeholder = DZ_PLACEHOLDERS[fieldName]();
        } else if (input.dataset.origPlaceholder) {
            input.placeholder = input.dataset.origPlaceholder;
            delete input.dataset.origPlaceholder;
        }
    }

    return allFound;
}

patch(FormController.prototype, {
    setup() {
        super.setup();

        let _tid = null;

        const scheduleUpdate = () => {
            const root = this.model?.root;
            if (!root || root.resModel !== "res.partner") return;

            // Debounce: cancel pending update so only the latest render wins.
            clearTimeout(_tid);
            _tid = setTimeout(() => {
                const formEl = document.querySelector(
                    ".o_action_manager .o_form_view"
                );
                if (!formEl) return;

                const allFound = applyDzPlaceholders(formEl);

                // city_id may not be rendered yet right after Algeria is selected
                // (Odoo re-renders the address block when enforce_cities becomes true).
                // Retry once after a longer delay.
                if (!allFound) {
                    _tid = setTimeout(() => {
                        const formEl2 = document.querySelector(
                            ".o_action_manager .o_form_view"
                        );
                        if (formEl2) applyDzPlaceholders(formEl2);
                    }, 500);
                }
            }, 250);
        };

        onMounted(scheduleUpdate);
        onPatched(scheduleUpdate);
    },
});
