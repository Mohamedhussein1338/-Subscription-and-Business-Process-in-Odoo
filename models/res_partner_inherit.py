from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    activation = fields.Boolean(string='Active')
