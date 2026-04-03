# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('state_id')
    def _onchange_state_id_dz(self):
        if self.country_id and self.country_id.code == 'DZ':
            self.city_id = False
