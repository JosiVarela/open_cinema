# -*- coding: utf-8 -*-
{
    'name': "Opencinema",

    'summary':"""
        Este es un módulo de gestión de cine
    """,

    'description': """
        Programa de gestión de películas
    """,

    'author': "Josi Varela",
    'website': "http://josivarela.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/opencinema.xml',
    ],
    'application':True,
    'demo':[
        'demo/demo.xml'
    ],
}