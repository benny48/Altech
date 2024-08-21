from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.registration'
    _description = 'Material Registration'

    code = fields.Char(string='Material Code', required=True)
    name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('material.supplier', string='Related Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        if self.buy_price < 100:
            raise ValidationError("Material Buy Price cannot be less than 100.")
