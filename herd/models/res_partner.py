# copyright 2022 Syera BONNEAUX @ Akretion

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.depends("herd_ids")
    def _compute_herd_count(self):
        for rec in self:
            rec.herd_count = len(rec.herd_ids)

    herd_ids = fields.One2many(
        comodel_name="herd", inverse_name="partner_id", string="Herds"
    )
    herd_count = fields.Integer(
        compute=_compute_herd_count, string="Number of herds", store=True
    )

    def action_view_herds(self):
        xmlid = "herd.action_herd"
        action = self.env["ir.actions.act_window"]._for_xml_id(xmlid)
        if self.herd_count > 1:
            action["domain"] = [("id", "in", self.herd_ids.ids)]
        else:
            action["views"] = [(self.env.ref("herd.view_herd_form").id, "form")]
            action["res_id"] = self.herd_ids and self.herd_ids.ids[0] or False
        return action
