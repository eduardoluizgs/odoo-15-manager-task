# # -*- coding: utf-8 -*-

# import pytz

# from odoo import http, fields
# from odoo.exceptions import ValidationError


# class IntegrationController(http.Controller):

#     @http.route('/api/integration/configs', auth='user', type='json')
#     def handler_configs(self):

#         event_sources = http.request.env['master.integration.event.source'].search([
#             ('active', '=', True)
#         ])

#         result = {}
#         for source in event_sources:
#             result.update({
#                 source.source_name: {
#                     'primary_keys': source.keys.split(','),
#                     'full_load': source.full_load
#                 }
#             })

#         return result

#     @http.route('/api/integration/events', auth='user', type='json')
#     def handler_event(self, data):

#         # check if data is valid format
#         if not isinstance(data, list) or not data:
#             raise ValidationError(u'O parâmetro `data` deve ser informado como uma lista de objetos!')

#         results = []
#         event = http.request.env['master.integration.event']

#         # for each row in data
#         for row in data:

#             source_id = None
#             try:

#                 # validate data
#                 source_id = row.get('source_id', None)
#                 if not source_id:
#                     raise ValidationError('Id de integração inválido!')

#                 source_name = row.get('source_name', None)
#                 if not source_name:
#                     raise ValidationError('Origem de integração inválida! Registro {}!'.format(source_id))

#                 operation = row.get('operation', None)
#                 if not operation:
#                     raise ValidationError('Operação de integração inválida! Registro {}!'.format(source_id))

#                 event_date = row.get('event_date', None)
#                 if not event_date:
#                     raise ValidationError('Data do evento inválida! Registro {}!'.format(source_id))

#                 timezone = pytz.timezone(http.request.env.context.get('tz') or http.request.env.user.tz or 'UTC')
#                 t = timezone.localize(fields.Datetime.from_string(event_date))
#                 event_date = t.astimezone(pytz.UTC)

#                 content = row.get('content', None)
#                 if not content:
#                     raise ValidationError('Conteudo da integração inválido! Registro {}!'.format(source_id))

#                 # check if record already exists
#                 event = event.search([('source_id', '=', source_id)])
#                 if not event:
#                     event = event.create({
#                         'source_id': source_id,
#                         'source_name': source_name,
#                         'operation': operation,
#                         'event_date': event_date.strftime('%Y-%m-%d %H:%M:%S')
#                     })
#                 event.write({
#                     'content': content
#                 })

#                 results.append({
#                     'sucess': True,
#                     'source_id': source_id,
#                     'message': 'OK'
#                 })

#             except Exception as e:
#                 results.append({
#                     'sucess': False,
#                     'source_id': source_id,
#                     'message': str(e)
#                 })
#                 # TODO : Add log here

#         return results
