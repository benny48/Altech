from odoo import models, fields, api

class MaterialSupplier(models.Model):
    _name = 'material.supplier'
    _description = 'Material Supplier'

    name = fields.Char(string='Supplier Name', required=True)
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone Number')
