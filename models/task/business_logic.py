# -*- coding: utf-8 -*-

from odoo import api, models, fields, tools, _
from odoo.exceptions import ValidationError


class IntegrationEventSourceBusinessLogic(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'manager.task.task'
    _inherit = ['manager.task.task']

    # ----------------------------------------------------
    # Compute
    # ----------------------------------------------------

    # TODO : Add business logic here
