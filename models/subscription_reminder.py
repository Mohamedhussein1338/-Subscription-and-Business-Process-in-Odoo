from odoo import models, fields, api
from datetime import datetime, timedelta

class SubscriptionReminder(models.Model):
    _name = 'subscription.reminder'
    _description = 'Subscription Renewal Reminder'

    subscription_id = fields.Many2one('sale.subscription', string='Subscription', required=True)
    subscription_template_id = fields.Many2one('sale.subscription.template', string='Subscription Template')
    customer_email = fields.Char(string='Customer Email', related='subscription_id.partner_id.email')
    subscription_start_date = fields.Date('Subscription Start Date')
    subscription_end_date = fields.Date('Subscription End Date')
    email_sent = fields.Boolean('Email Sent', default=False)
    days_remaining = fields.Integer('Days Remaining', compute='_compute_days_remaining', store=True)

    @api.depends('subscription_end_date')
    def _compute_days_remaining(self):
        for record in self:
            if record.subscription_end_date:
                today = fields.Date.today()
                remaining_days = (record.subscription_end_date - today).days
                record.days_remaining = max(0, remaining_days)
            else:
                record.days_remaining = 0


    def send_subscription_email(self):
            domain = [
                ('subscription_template_id', '=', 'Monthly Subscription'),
                ('days_remaining', '=', 7),
                ('email_sent', '=', False),
            ]

            subscriptions_to_notify = self.search(domain)

            for subscription in subscriptions_to_notify:
                subscription.write({'email_sent': True})

                # Send email using the specified email template
                template = self.env.ref('subscription.email_template_subscription_reminder')
                template.send_mail(subscription.id)

                # Print a test message
                print('Email sent for subscription:', subscription.id)






