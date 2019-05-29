from odoo import models, fields, api
class x_penalties(models.Model):
	pemployee = fields.Many2one('hr.employee', 'employee')
	pfinetype = fields.Many2one('x.fine','fine type')
	pfineamount = fields.Integer("enter fine amount")
	pdatefrom = fields.Date("enter effective date from")
	pdateto = fields.Date("enter effective date to")