from odoo import api, models, fields, tools, _
from odoo.exceptions import ValidationError


class TaskTypeBusinessLogic(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'manager.task.project'
    _inherit = ['manager.task.project']

    # ----------------------------------------------------
    # Compute
    # ----------------------------------------------------

    # TODO : Add business logic here
