# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class Physiology(models.Model):
    _name = "physiology"
    _description = "Physiology"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer()
    active = fields.Boolean(default=True)

    _sql_constraints = [("name_unique", "UNIQUE(name)", "Field name must be unique")]
