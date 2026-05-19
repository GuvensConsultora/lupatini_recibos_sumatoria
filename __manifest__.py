{
    'name': 'Lupatini — Sumatoria en pestaña Deudas del recibo',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Localizations/Argentina',
    'summary': 'Agrega total al pie de la columna "Monto" en la pestaña Deudas del recibo (account.payment.group). Sólo extiende la vista, sin tocar lógica del módulo OCA account_payment_group.',
    'author': 'Yagüven C.G.',
    'license': 'AGPL-3',
    'depends': [
        'account_payment_group',
    ],
    'data': [
        'views/account_payment_group_views.xml',
    ],
    'installable': True,
    'application': False,
}
