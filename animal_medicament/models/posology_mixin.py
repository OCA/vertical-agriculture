# © 2023 David BEAL @ Akretion

from odoo import fields, models

MILK = [
    ("day", "Day"),
    ("hour", "Hour"),
    ("milking", "Milking"),
    ("forbidden", "Forbidden"),
]
MEAT = [
    ("day", "Day"),
    ("hour", "Hour"),
    ("forbidden", "Forbidden"),
]


class PosologyMixin(models.AbstractModel):
    _name = "posology.mixin"
    _description = "Posology fields used in Posology and Prescription"

    unit_milk = fields.Selection(selection=MILK, default="milking")
    unit_meat = fields.Selection(selection=MEAT, default="day")
    milk_time = fields.Char(
        string="Milk time", help="Waiting time for milk case by unit"
    )
    meat_time = fields.Char(
        string="Meat time", help="Waiting time for meat case by unit"
    )
