# -*- coding: utf-8 -*-

from odoo import models, fields


class IntegrationEventSourceModel(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'manager.task.task'
    _description = 'Tarefas'
    _order = "name"

    # ----------------------------------------------------
    # Fields
    # ----------------------------------------------------

    name = fields.Char(
        strig='Descrição',
        size=255,
        required=True
    )

    # source_system = fields.Selection(
    #     string='Sistema de Origem',
    #     selection=[
    #         ('MasterComV2', 'Master.com v2'),
    #         ('MasterComV3', 'Master.com v3'),
    #     ],
    #     help=u'Informa o sistema de origem da integração',
    #     required=True
    # )

    # source_name = fields.Char(
    #     string='Chave da Origem',
    #     size=50,
    #     help=u'Informa a chave de identificação da origem da integração',
    #     required=True
    # )

    # keys = fields.Char(
    #     string='Campos Chaves',
    #     size=50,
    #     help=u'''
    #         Informa os campos que iráo compor a chave de integração do registro.
    #         Normalmente os campos representam as chaves primárias da tabelas.
    #         Exemplo: CodigoDoPais,CodigoDaEmpresa
    #     ''',
    #     required=True
    # )

    # active = fields.Boolean(
    #     string='Ativo?',
    #     help='Informa se a origem está ativa na sincronização',
    #     default=False
    # )

    # full_load = fields.Boolean(
    #     string='Carga Completa?',
    #     help='Informa se a origem deve realizar uma carga completa durante a integração',
    #     default=False
    # )
