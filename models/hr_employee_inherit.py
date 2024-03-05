from odoo import models, fields, api, exceptions

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    active = fields.Boolean()

    def write(self, vals):
        res = super(HREmployee, self).write(vals)

        if 'active' in vals:
            active = vals['active']
            for employee in self:
                partner = employee.address_home_id
                if partner:
                    partner.write({'active': active})

        return res




