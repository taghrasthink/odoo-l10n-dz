# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    name = fields.Char(translate=True)

    city_ids = fields.One2many(
        'res.city',
        'state_id',
        string='Communes',
    )
