
{
    'name': 'Information System Audit',
    'category': 'Extra Tools',
    'version': '1.0',
    'sequence': 3,
    'summary': '',
    'website': 'http://metalogic.com/',
    'description': 'Menu Informasi System Audit For Aggio',
    'author': 'ABBAS e-mail==>> abdul_basith6@yahoo.co.id',
    'depends': ['base','mi_season'],
    'data': [
        'security/res_groups_system_audit.xml',
        'security/ir.model.access.csv',
        'views/audit_wkf.xml',
        'views/data_audit_view.xml',
        'views/informasi_data_audit_view.xml',
        'views/informasi_data_audit_detail_view.xml',
        'views/reminder_audit_view.xml',
        'edi/action_data_reminder_audit.xml',
        'report/rpt_audit.xml',
    ],
    'installable': True,
    'auto_install': False,
#     'bootstrap': True, # load translations for login screen
    'application': True,
}
