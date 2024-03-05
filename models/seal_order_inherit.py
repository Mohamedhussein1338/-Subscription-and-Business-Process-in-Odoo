from odoo import models, fields, api
from odoo.odoo import exceptions
from odoo.odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_confirmed = fields.Boolean(string='Is Confirmed',compute="_compute_is_confirmed", default=False,  store=True)

    @api.depends('state')
    def _compute_is_confirmed(self):
        for order in self:
            order.is_confirmed = order.state == 'sale'


    def write(self, vals):
        if self.state == 'sale':
            raise exceptions.UserError("Cannot update the order when it is confirmed.")
        return super(SaleOrder, self).write(vals)
