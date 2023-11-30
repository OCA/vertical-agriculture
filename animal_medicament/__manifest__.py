# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Animal Medicament",
    "version": "14.0.1.1.0",
    "category": "Tools",
    "website": "https://github.com/OCA/vertical-agriculture",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["bealdav"],
    "license": "AGPL-3",
    "installable": True,
    "summary": "Drug posologies definition for animals",
    "depends": [
        "product",
        "animal",
    ],
    "data": [
        "views/posology.xml",
        "views/product.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
}
