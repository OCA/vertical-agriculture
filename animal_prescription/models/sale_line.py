# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import defaultdict

from odoo import api, fields, models

from odoo.addons.animal_medicament.models.posology_mixin import MEAT, MILK


class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = ["sale.order.line", "posology.mixin"]

    unit_milk = fields.Selection(selection=MILK)
    unit_meat = fields.Selection(selection=MEAT)
    animal_count = fields.Integer(string="Headcount", help="Animals number")
    animal_ids = fields.Many2many(comodel_name="animal", string="Animals")
    physiology_id = fields.Many2one(comodel_name="physiology")
    posology_id = fields.Many2one(
        comodel_name="posology", compute="_compute_posology", store=True
    )
    poso_description = fields.Text()
    specie_id = fields.Many2one(comodel_name="animal.species")
    parent_specie_id = fields.Many2one(related="order_id.herd_id.specie_id")
    lot_name = fields.Char(related="lot_id.name")
    lot_date = fields.Date(related="lot_id.expiry_date")
    product_tracking = fields.Selection(related="product_id.tracking")
    milk_time_str = fields.Char(
        string="Milk Delay",
        compute="_compute_time_fields",
        readonly=False,
        store=True,
        help="Waiting time for milk case by unit",
    )
    meat_time_str = fields.Char(
        string="Meat Delay",
        compute="_compute_time_fields",
        readonly=False,
        store=True,
        copy=False,
        help="Waiting time for meat case by unit",
    )

    @api.depends(
        "product_id", "physiology_id", "order_id.herd_id", "milk_time", "meat_time"
    )
    def _compute_time_fields(self):
        for rec in self:
            rec.milk_time_str = rec.milk_time
            rec.meat_time_str = rec.meat_time

    @api.depends("product_id", "physiology_id", "order_id.herd_id")
    def _compute_posology(self):
        poso_prd = defaultdict(dict)
        order = self[0].order_id
        if order and order.herd_id:
            products = self.mapped("product_id")
            posos = self.env["posology"].search(
                self._get_posology_domain(products),
                order="product_id, physiology_id DESC",
            )
            for poso in posos:
                if poso.description:
                    poso_prd[poso.product_id][poso.physiology_id or "no"] = poso
        for rec in self:
            if rec.product_id in poso_prd:
                posology = poso_prd[rec.product_id].get(rec.physiology_id) or poso_prd[
                    rec.product_id
                ].get("no")
                rec.posology_id = posology or False
                rec.unit_milk = posology.unit_milk
                rec.milk_time = posology.milk_time
                rec.unit_meat = posology.unit_meat
                rec.meat_time = posology.meat_time
                rec.poso_description = posology.description
            else:
                rec.posology_id = False

    def _get_posology_domain(self, products):
        return [
            ("product_id", "in", products.ids),
            ("specie_id", "child_of", self[0].order_id.herd_id.specie_id.id),
        ]

    def get_animals(self):
        for rec in self:
            rec.animal_ids = rec.order_id.animal_ids

    def get_sale_order_line_multiline_description_sale(self, product):
        res = super().get_sale_order_line_multiline_description_sale(product)
        if res and res[:1] == "[":
            pos = res.find("]")
            if pos != -1:
                res = res[pos + 2 :]
        return res
