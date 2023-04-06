# © 2021 David BEAL @ Akretion

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    posology_ids = fields.One2many(
        comodel_name="posology", inverse_name="product_id", string="Posology"
    )
    therapist_code = fields.Char()
    market_authorization = fields.Char(help="Authorization to market")
    medical_register_link = fields.Char()
    issue_condition = fields.Selection(selection=[], help="Conditions of issue")
