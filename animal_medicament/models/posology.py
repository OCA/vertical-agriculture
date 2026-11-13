# © 2021 David BEAL @ Akretion

from odoo import fields, models

from .posology_mixin import MEAT, MILK


class Posology(models.Model):
    _name = "posology"
    _inherit = ["posology.mixin"]
    _description = "Posology for medical devices"
    _rec_name = "description"
    _order = "product_id"

    unit_milk = fields.Selection(selection=MILK)
    unit_meat = fields.Selection(selection=MEAT)
    description = fields.Text(required=True)
    specie_id = fields.Many2one(comodel_name="animal.species", string="Specie")
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product", required=True
    )
    categ_id = fields.Many2one(
        comodel_name="product.category",
        related="product_id.categ_id",
        store=True,
        string="Category",
    )
    administered_dose = fields.Float()
    frequency = fields.Float(help="Number of times per unit of time")
    interval = fields.Float()
    duration = fields.Float()

    def _duplicate(self):
        active_ids = self.env.context.get("active_ids")
        if active_ids:
            for rec in self.browse(active_ids):
                rec.copy()

    def copy_data(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if self.description:
            default.update(description="%s /copy" % self.description)
        return super().copy_data(default)
