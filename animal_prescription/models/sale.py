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

    @api.onchange("partner_id")
    def _onchange_default_herd_id(self):
        if self.partner_id and len(self.partner_id.herd_ids) == 1:
            self.herd_id = self.partner_id.herd_ids.id
        else:
            self.herd_id = False
