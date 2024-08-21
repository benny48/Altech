from odoo.tests.common import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['material.supplier'].create({'name': 'Test Supplier'})
        self.material = self.env['material.registration'].create({
            'code': 'MAT01',
            'name': 'Test Material',
            'material_type': 'fabric',
            'buy_price': 150,
            'supplier_id': self.supplier.id,
        })

    def test_material_creation(self):
        self.assertEqual(self.material.code, 'MAT01')
        self.assertEqual(self.material.name, 'Test Material')

    def test_material_buy_price_validation(self):
        with self.assertRaises(ValidationError):
            self.material.write({'buy_price': 50})
