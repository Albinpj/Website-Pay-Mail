{
    'name': 'Pay Mail',
    'version': '15.0.1.0',
    'sequence': -3000,
    'category': 'Website Pay Mail',
    'summary': 'Send A Mail At The Time Of Paying',
    'application': True,
    'depends': [
        'base',
        'mail',
        'contacts',
        'sale_management',
        'website',

    ],
    'data': [
        'data/pay_mail_template.xml',
    ],

}
