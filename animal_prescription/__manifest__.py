# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Animal Prescriptions",
    "version": "14.0.1.0.0",
    "category": "Sales",
    "website": "https://github.com/OCA/vertical-agriculture",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["bealav"],
    "license": "AGPL-3",
    "installable": True,
    "summary": "Management of prescriptions for veterinarians",
    "depends": [
        "herd",
        "sale_management",
        "animal_medicament",
        "sale_order_lot_selection",
        "product_expiry_simple",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale.xml",
        "views/product.xml",
        "views/physiology.xml",
        "views/herd.xml",
    ],
    "demo": [
        "data/physiology.csv",
        "data/settings.xml",
    ],
}
