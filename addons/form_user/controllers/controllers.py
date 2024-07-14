# -*- coding: utf-8 -*-
# from odoo import http


# class FormUser(http.Controller):
#     @http.route('/form_user/form_user', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/form_user/form_user/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('form_user.listing', {
#             'root': '/form_user/form_user',
#             'objects': http.request.env['form_user.form_user'].search([]),
#         })

#     @http.route('/form_user/form_user/objects/<model("form_user.form_user"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('form_user.object', {
#             'object': obj
#         })
