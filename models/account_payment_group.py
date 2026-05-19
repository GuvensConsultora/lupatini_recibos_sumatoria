from odoo import api, fields, models


class AccountPaymentGroup(models.Model):
    _inherit = 'account.payment.group'

    debt_total_amount = fields.Monetary(
        string='Deuda Total',
        currency_field='currency_id',
        compute='_compute_debt_total_amount',
    )

    @api.depends('debt_move_line_ids')
    def _compute_debt_total_amount(self):
        for rec in self:
            rec.debt_total_amount = sum(
                rec.debt_move_line_ids.mapped('amount_residual')
            )
