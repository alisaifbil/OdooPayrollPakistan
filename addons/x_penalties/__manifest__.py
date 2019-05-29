# -*- coding: utf-8 -*-
{
    'name': "Penalties Extension",

    'summary': """
       to map fines to employees""",

    'description': """
        to fine employees
    """,

    'author': "Sajjad Wazir",
    'website': "http://www.notSajjad.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Payroll',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/x_penalties_views.xml'
        
    ],
}