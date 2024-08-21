from odoo import http

class MaterialController(http.Controller):

    @http.route('/material', type='http', auth='public', methods=['GET'], csrf=False)
    def get_materials(self, **kwargs):
        materials = http.request.env['material.registration'].sudo().search([])
        return http.request.render('module_name.template_name', {'materials': materials})
