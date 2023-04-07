# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class Posology(models.Model):
    _inherit = "posology"

    physiology_id = fields.Many2one(comodel_name="physiology")
