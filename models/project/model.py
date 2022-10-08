from odoo import models, fields


class ProjectModel(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'manager.task.project'
    _description = 'Projetos'
    _order = "name"

    # TODO : Add create index for source_name, source_id and operation

    # ----------------------------------------------------
    # Fields
    # ----------------------------------------------------

    name = fields.Char(
        strig='Nome do Projeto',
        size=100,
        store=True
    )

    # source_id = fields.Integer(
    #     string='Id da Origem',
    #     help=u'Informa o id de origem da integração',
    #     required=True,
    #     index=True
    # )

    # source_name = fields.Char(
    #     string='Origem',
    #     size=50,
    #     help=u'Informa a origem da integração',
    #     required=True
    # )

    # operation = fields.Selection(
    #     string='Operação',
    #     selection=[
    #         ('Insert', 'Inserção'),
    #         ('Update', 'Atualização'),
    #         ('Delete', 'Remoção')
    #     ],
    #     help=u'Informa o tipo da operação de integração',
    #     required=True
    # )

    # event_date = fields.Datetime(
    #     string='Data do Evento',
    #     help='Informa a data que ocorreu o evento. Necessário para ordenar o processamento dos eventos.',
    #     required=True
    # )

    # content = fields.Text(
    #     string=u'Conteúdo',
    #     help=u'Informa o conteúdo da integração'
    # )

    # processed = fields.Boolean(
    #     string='Processado?',
    #     help='Informa se o registro já foi processado pelo sistema',
    #     default=False
    # )

    # processed_date = fields.Datetime(
    #     string='Processado em',
    #     help='Informa a data de processamento do registro'
    # )
