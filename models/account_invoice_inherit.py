from odoo import models, api,fields
from lxml import etree

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    is_confirmed = fields.Boolean(string='Is Confirmed')

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(AccountInvoice, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                            submenu=submenu)

        doc = etree.XML(res['arch'])

        if view_type == 'form':
            for node in doc.xpath("//field"):
                field_name = node.get('name', '')

                node.set('attrs', "{'readonly': [('is_confirmed', '=', True)]}")

        res['arch'] = etree.tostring(doc)
        return res