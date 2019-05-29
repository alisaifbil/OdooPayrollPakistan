from odoo import models, fields, api
class x_fine(models.Model):
    _name = 'x.fine'
    name = fields.Char("enter fine type")
    _amount = 'x.fine'
    amount = fields.Char("enter fine amount")