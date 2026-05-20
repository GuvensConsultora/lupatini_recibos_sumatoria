{
    'name': 'Lupatini — Sumatoria en pestaña Deudas del recibo',
    'version': '17.0.1.3.0',
    'category': 'Accounting/Localizations/Argentina',
    'summary': 'Muestra la deuda total del partner ("Deuda Total") al abrir el recibo, sumando amount_residual de debt_move_line_ids. Adicionalmente agrega sum=Total a la columna "Monto" del listado (sólo aplica en pestaña Líneas de pagos, que es store=True).',
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
