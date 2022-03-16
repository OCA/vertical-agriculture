# copyright 2022 David BEAL @ Akretion

from odoo import api, fields, models


class Herd(models.Model):
    _name = "herd"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Herd Inventory"
    _rec_name = "display_name"

    display_name = fields.Char(
        "Display Name", compute="_compute_display_name", store=True
    )
    name = fields.Char(string="Livestock")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Owner")
    specie_id = fields.Many2one(
        comodel_name="animal.species",
        string="Specie",
        required=True,
        domain=[("level", "=", 1)],
    )
    breed_id = fields.Many2one(
        comodel_name="animal.breed",
        string="Breed",
    )
    animal_ids = fields.One2many(
        comodel_name="animal", inverse_name="herd_id", string="Animal"
    )

    @api.depends("partner_id", "specie_id", "breed_id", "name")
    def _compute_display_name(self):
        def name(rec, field):
            if rec[field]:
                if field == "name":
                    return rec.name
                return rec[field]["name"]
            else:
                return ""

        for rec in self:
            partner, specie, breed, name = (
                name(rec, "partner_id"),
                name(rec, "specie_id"),
                name(rec, "breed_id"),
                name(rec, "name"),
            )
            rec.display_name = f"{partner}: {specie}, {breed} {name}"

    @api.onchange("specie_id")
    def breed_onchange(self):
        for rec in self:
            if rec.breed_id.species_id != rec.specie_id:
                rec.breed_id = False
