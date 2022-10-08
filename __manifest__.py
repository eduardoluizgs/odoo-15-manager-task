# -*- encoding: utf-8 -*-
{
    'name': 'Manager - Task',
    'summary': 'Módulo de gerenciamento de tarefas',
    'version': '15.0.0.0',
    'category': 'Manager',
    'summary': """

    """,
    'author': "Unknow",
    'website': '',
    'license': 'AGPL-3',
    'depends': [],
    'data': [
        'security/ir.rules.access.xml',
        'security/ir.model.access.csv',
        'views/project.xml',
        'views/task.xml',
        'views/app.xml',
        'data/project.xml'
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True
}
