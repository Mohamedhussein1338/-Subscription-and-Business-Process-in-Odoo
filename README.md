# Subscription and Business Process in Odoo
This repository contains customizations and enhancements for an Odoo implementation, focusing on improving subscription management, CRM processes, employee creation, payment reports, and sales order confirmations. The following features have been implemented:

1-Subscription Reminder Email:

A monthly subscription feature that sends customers an email notification 7 days before the next invoice date.
Provides users with the option to renew or cancel their subscription conveniently.
CRM Lead to Project Automation:

2-Automatically creates a project in Odoo when a new lead is created in crm.lead.
Streamlines the process of converting leads into actionable projects.
Employee and Contact Integration:

3-Upon creating an employee in hr.employee, a corresponding contact is automatically generated.
Introduces an 'active' field in both hr.employee and res.partner to control the visibility and update behavior.
If 'active' is set to true during employee creation, it updates the 'active' status in res.partner and sets the attribute as 'readonly'.
Customized Payment PDF Report:

4-Inherits the payment PDF report and adds a prominent "Odoo 17" text in the center.
Enhances the visual identity of payment reports for Odoo version 17.
Sales Order Confirmation Enhancement:

5-Implements a feature in sale.order where clicking the 'confirm' button renders all fields as 'readonly'.
Ensures data integrity and prevents unintentional modifications after order confirmation.


