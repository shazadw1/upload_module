{
    'name': 'Upload Module',
    'version': '15.6.1',
    'description': 'Upload Modules by goinig to from Settings -> Upload Module -> Upload Module',
    'category': 'app',
    'website': "https://softwareescarlata.com/",
    'summary': """
    upload
    module 
    ftp
    Upload Modules by goinig to from Settings -> Upload Module -> Upload Module""",
    'author': 'David Montero Crespo',
    'depends': ['web'],
    'price': 15,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': True,
    'images':[
        'static/description/1.png',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/upload_module.xml',

    ]
}
