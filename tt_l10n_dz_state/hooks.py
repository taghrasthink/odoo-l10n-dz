# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

import logging

_logger = logging.getLogger(__name__)

DZ_STATE_AR_NAMES = {
    '01': 'أدرار',
    '02': 'الشلف',
    '03': 'الأغواط',
    '04': 'أم البواقي',
    '05': 'باتنة',
    '06': 'بجاية',
    '07': 'بسكرة',
    '08': 'بشار',
    '09': 'البليدة',
    '10': 'البويرة',
    '11': 'تمنراست',
    '12': 'تبسة',
    '13': 'تلمسان',
    '14': 'تيارت',
    '15': 'تيزي وزو',
    '16': 'الجزائر',
    '17': 'الجلفة',
    '18': 'جيجل',
    '19': 'سطيف',
    '20': 'سعيدة',
    '21': 'سكيكدة',
    '22': 'سيدي بلعباس',
    '23': 'عنابة',
    '24': 'قالمة',
    '25': 'قسنطينة',
    '26': 'المدية',
    '27': 'مستغانم',
    '28': 'المسيلة',
    '29': 'معسكر',
    '30': 'ورقلة',
    '31': 'وهران',
    '32': 'البيض',
    '33': 'إليزي',
    '34': 'برج بوعريريج',
    '35': 'بومرداس',
    '36': 'الطارف',
    '37': 'تندوف',
    '38': 'تيسمسيلت',
    '39': 'الوادي',
    '40': 'خنشلة',
    '41': 'سوق أهراس',
    '42': 'تيبازة',
    '43': 'ميلة',
    '44': 'عين الدفلى',
    '45': 'النعامة',
    '46': 'عين تموشنت',
    '47': 'غرداية',
    '48': 'غليزان',
    '49': 'تيميمون',
    '50': 'برج باجي مختار',
    '51': 'أولاد جلال',
    '52': 'بني عباس',
    '53': 'عين صالح',
    '54': 'عين قزام',
    '55': 'تقرت',
    '56': 'جانت',
    '57': 'المغير',
    '58': 'المنيعة',
    '59': 'أفلو',
    '60': 'الأبيض سيدي الشيخ',
    '61': 'العريشة',
    '62': 'القنطرة',
    '63': 'بريكة',
    '64': 'بوسعادة',
    '65': 'بير العاتر',
    '66': 'قصر البخاري',
    '67': 'قصر الشلالة',
    '68': 'عين وسارة',
    '69': 'مسعد',
}


def _apply_ar_translations(env):
    """Apply Arabic translations for all DZ wilayas.

    Uses a single write() per state to avoid N+1 queries.
    Returns the number of states updated.
    """
    ar_lang = env['res.lang'].search([('code', '=', 'ar_001')], limit=1)
    if not ar_lang:
        ar_lang = env['res.lang'].search([('code', 'like', 'ar%')], limit=1)
    if not ar_lang:
        _logger.info("Arabic language not installed, skipping DZ state translations.")
        return 0

    lang_code = ar_lang.code
    states = env['res.country.state'].search([('country_id.code', '=', 'DZ')])
    count = 0
    for state in states:
        ar_name = DZ_STATE_AR_NAMES.get(state.code)
        if ar_name:
            state.with_context(lang=lang_code).name = ar_name
            count += 1
    return count


def post_init_hook(env):
    """Set Arabic translations for Algerian wilayas.

    This hook is needed because Odoo's base module may already create
    some DZ states with its own XML IDs, making .po translations
    (which reference our module's XML IDs) ineffective for those records.
    """
    count = _apply_ar_translations(env)
    if count:
        _logger.info("Set Arabic translations for %d Algerian wilayas.", count)


def uninstall_hook(env):
    """Reset enforce_cities on Algeria to avoid broken address forms."""
    country = env.ref('base.dz', raise_if_not_found=False)
    if country:
        country.enforce_cities = False
        _logger.info("tt_l10n_dz_state: reset enforce_cities on Algeria.")
