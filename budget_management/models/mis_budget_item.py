# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, _


class MisBudgetItem(models.Model):
    _inherit = 'mis.budget.item'

    budget_plan_id = fields.Many2one(
        comodel_name='budget.plan',
        ondelete='cascade',
        index=True,
    )
    active = fields.Boolean(
        related='budget_plan_id.active',
        readonly=True,
    )
