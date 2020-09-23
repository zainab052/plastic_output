# -*- coding: utf-8 -*-
{
    'name': "plastic_output",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/plastic_security.xml',
        'security/ir.model.access.csv',
        'views/plastic_machine_views.xml',
        'views/plastic_data_views.xml',
        'views/plastic_menu_views.xml',
        'reports/reports.xml',
        'reports/report_plastic_details.xml',
        'wizard/plastic_data_wizard.xml',
    ],
}
