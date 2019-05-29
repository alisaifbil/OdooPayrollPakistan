# -*- coding: utf-8 -*-
{
    'name': "Fine Module",

    'summary': """
       to define fine types""",

    'description': """
        defining fine types
    """,

    'author': "Alisaif Bilgrami",
    'website': "http://www.notali.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Payroll',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/x_fine_type_view.xml'
        
    ],
}