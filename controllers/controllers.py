# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import base64
import requests


class ImageUrl(http.Controller):

    @http.route('/base_64_to_url/<string:model_name>/<string:image_field_name>/<int:id>', auth='public', type='http',
                csrf=False,
                methods=['GET'], cors='*')
    def downloadDocument(self, model_name=False, image_field_name=False, id=False, **kwargs):

        # Hremployee = request.env['hr.employee']
        model = request.env[model_name]
        model_row = model.sudo().search([('id', '=', int(id))])

        if model_row[image_field_name]:
            return Response(base64.b64decode(model_row[image_field_name]), headers={'content-type': 'application/pdf',
                                                                                    'Content-Length': len(
                                                                                        model_row[image_field_name]),
                                                                                    'Content-Disposition': 'inline; filename="' +
                                                                                                           model_row[
                                                                                                               'name'] + '.pdf"'})
        else:
            return "There is no certificate to visible please upload your certificate"

        # return Response(base64.b64decode(model_row[image_field_name]),
        #                 headers={'content-type': 'image/jpeg', 'Content-Length': len(model_row[image_field_name]),
        #                          'Content-Disposition': 'inline; filename="' + model_row['name'] + '.png"'},
        #                 status=200)
        # Return pdf file
