# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.
{
    'name': 'Algeria - Administrative Division',
    'version': '17.0.4.1.0',
    'category': 'Localization',
    'summary': 'Administrative Division of Algeria (2025)',
    'description': """
Algeria Localization - Administrative Division 2025
=====================================================

This module provides the updated Algerian administrative division:

* **69 States** (states/provinces) linked to Algeria
* **1541 Cities** (cities/municipalities) linked to their wilaya
* **Arabic translations** for all wilaya and commune names

Data sourced from https://github.com/S450R1/algeria-cities-2025
""",
    'author': 'TaghrasThink',
    'website': 'https://github.com/taghrasthink',
    'license': 'LGPL-3',
    'depends': ['contacts', 'base_address_extended'],
    'data': [
        'data/res_country.xml',
        'data/res_country_state.xml',
        'data/res_cities.xml',
        'views/l10n_dz_views.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tt_l10n_dz_state/static/src/js/partner_address.js',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'application_type': 'anti_cache_force_base64_v130',
}
