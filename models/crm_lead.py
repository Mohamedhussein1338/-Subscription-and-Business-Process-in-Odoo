from odoo import models, fields, api
class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, values):
        # Call the original create method
        lead = super(CrmLead, self).create(values)

        # Create a project based on the lead
        project_vals = {
            'name': lead.name + ' Project',  # Adjust as needed
            'description': lead.description,
        }

        project = self.env['project.project'].create(project_vals)

        # You can associate the lead with the project if needed
        lead.write({'name': project.id})

        return lead
