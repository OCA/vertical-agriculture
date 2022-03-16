# copyright 2022 David BEAL @ Akretion

from odoo import fields, models


class Animal(models.Model):
    _inherit = "animal"
    _order = "id"

    herd_id = fields.Many2one(comodel_name="herd", string="Herd")
    mother_id = fields.Many2one(
        comodel_name="animal", string="Mother", domain="[('id', '!=', id)]"
    )
    father_id = fields.Many2one(
        comodel_name="animal", string="Father", domain="[('id', '!=', id)]"
    )
    breed_id = fields.Many2one(comodel_name="animal.breed", required=False)
    date_in_herd = fields.Date(string="Introduction Date", help="Herd introduction")
