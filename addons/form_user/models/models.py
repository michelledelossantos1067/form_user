# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class form_user(models.Model):
#     _name = 'form_user.form_user'
#     _description = 'form_user.form_user'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
