# copyright 2022 David BEAL @ Akretion

from odoo import api, fields, models


class AnimalSpecies(models.Model):
    _inherit = "animal.species"

    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = "name"
    _order = "complete_name"

    name = fields.Char(index=True, required=True)
    complete_name = fields.Char(
        string="Family / Specie", compute="_compute_complete_name", store=True
    )
    parent_id = fields.Many2one(
        comodel_name="animal.species",
        string="Parent Specie",
        index=True,
        ondelete="cascade",
    )
    parent_path = fields.Char(index=True)
    level = fields.Integer(compute="_compute_level", store=True)
    child_ids = fields.One2many(
        comodel_name="animal.species", inverse_name="parent_id", string="Child Species"
    )

    @api.depends("parent_path")
    def _compute_level(self):
        for rec in self:
            rec.level = len([x for x in rec.parent_path if "/" in x])

    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for specie in self:
            if specie.parent_id:
                specie.complete_name = "%s / %s" % (
                    specie.parent_id.complete_name,
                    specie.name,
                )
            else:
                specie.complete_name = specie.name
