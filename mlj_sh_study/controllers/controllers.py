# -*- coding: utf-8 -*-
from odoo import http

# class MljShStudy(http.Controller):
#     @http.route('/mlj_sh_study/mlj_sh_study/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mlj_sh_study/mlj_sh_study/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mlj_sh_study.listing', {
#             'root': '/mlj_sh_study/mlj_sh_study',
#             'objects': http.request.env['mlj_sh_study.mlj_sh_study'].search([]),
#         })

#     @http.route('/mlj_sh_study/mlj_sh_study/objects/<model("mlj_sh_study.mlj_sh_study"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mlj_sh_study.object', {
#             'object': obj
#         })