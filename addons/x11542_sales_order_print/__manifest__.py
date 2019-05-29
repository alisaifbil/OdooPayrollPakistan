# -*- coding: utf-8 -*-
{
    'name': "Sales Order Print",

    'summary': """
        Sales Order Print """,
    'description': """
      Sales Order Print
    """,
    'author': "AliSaif",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Report',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['sale','base','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       # 'views/views.xml',
       'reports/x11542_sales_order_print.xml',
    ],
}
