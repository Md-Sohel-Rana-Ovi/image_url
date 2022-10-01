# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class image_url(models.Model):
#     _name = 'image_url.image_url'
#     _description = 'image_url.image_url'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
