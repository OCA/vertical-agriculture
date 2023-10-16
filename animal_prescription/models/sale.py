# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    herd_id = fields.Many2one(comodel_name="herd", string="Herd")
    animal_ids = fields.Many2many(comodel_name="animal", string="Animals")
    total_quantity = fields.Float(
        compute="_compute_total_quantity", help="Used on report"
    )
    specie_id = fields.Many2one(related="herd_id.specie_id")

    @api.depends("order_line.product_uom_qty")
    def _compute_total_quantity(self):
        for rec in self:
            rec.total_quantity = sum(rec.order_line.mapped("product_uom_qty"))
