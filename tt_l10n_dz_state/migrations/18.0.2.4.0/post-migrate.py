# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

import logging
from odoo import api, SUPERUSER_ID
from odoo.addons.tt_l10n_dz_state.hooks import _apply_ar_translations

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Apply Arabic translations for Algerian wilayas."""
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    count = _apply_ar_translations(env)
    _logger.info("tt_l10n_dz_state: set Arabic names for %d wilayas.", count)
