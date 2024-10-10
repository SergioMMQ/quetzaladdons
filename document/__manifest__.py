# -*- coding: utf-8 -*-

{
    'name': 'Documentos',
    'summary':"""    Aplicacion para Documentos    """,
    'author': 'Sergio Martinez Meneses',
    'category': 'Informes',
    'version': '1.0.3',
    'depends': ['base','base_setup','web','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_view.xml',
        'views/document_menu.xml',
        'views/document_folder.xml',
        'views/document_search.xml',
        'views/revisiones_documentos.xml',
        ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
