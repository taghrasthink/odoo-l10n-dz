# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

import logging
from odoo import api, SUPERUSER_ID

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


def migrate(cr, version):
    """Apply Arabic translations for Algerian wilayas."""
    if not version:
        return

    env = api.Environment(cr, SUPERUSER_ID, {})

    # Find Arabic language
    ar_lang = env['res.lang'].search([('code', '=like', 'ar%')], limit=1)
    if not ar_lang:
        _logger.info("tt_l10n_dz_state: Arabic language not installed, skipping.")
        return

    lang_code = ar_lang.code
    _logger.info("tt_l10n_dz_state: applying Arabic (%s) translations for DZ wilayas...", lang_code)

    states = env['res.country.state'].search([('country_id.code', '=', 'DZ')])
    count = 0
    for state in states:
        ar_name = DZ_STATE_AR_NAMES.get(state.code)
        if ar_name:
            state.with_context(lang=lang_code).name = ar_name
            count += 1

    _logger.info("tt_l10n_dz_state: set Arabic names for %d/%d wilayas.", count, len(states))
