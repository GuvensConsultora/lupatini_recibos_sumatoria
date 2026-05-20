from odoo import api, fields, models


class AccountPaymentGroup(models.Model):
    _inherit = 'account.payment.group'

    debt_total_amount = fields.Monetary(
        string='Deuda Total',
        currency_field='currency_id',
        compute='_compute_debt_total_amount',
    )

    # Por qué `to_pay_move_line_ids.amount_residual` y no `debt_move_line_ids`:
    # `debt_move_line_ids` es un m2m computed sobre `to_pay_move_line_ids` sin
    # store, y el depends contra computed-no-stored no se retriggerea de forma
    # confiable cuando el usuario remueve líneas con la X (caso reportado por
    # Anael 2026-05-19: 4 facturas residual -$572.787 mostraban -$1.333.948).
    # `to_pay_move_line_ids` sí tiene tabla relacional propia
    # (`account_move_line_payment_group_to_pay_rel`), y al depender de
    # `.amount_residual` Odoo recalcula cuando cambia el set o el residual de
    # cualquiera de sus líneas. El signo replica la convención del OCA
    # `_compute_selected_debt`: proveedor = -1 (residuales negativos quedan en
    # positivo si el cliente quiere leer "cuánto debo pagar"), cliente = +1.
    @api.depends('to_pay_move_line_ids.amount_residual', 'partner_type')
    def _compute_debt_total_amount(self):
        for rec in self:
            sign = -1.0 if rec.partner_type == 'supplier' else 1.0
            rec.debt_total_amount = sign * sum(
                rec.to_pay_move_line_ids.mapped('amount_residual')
            )
