# Copyright (C) 2022 Akretion
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Herd",
    "version": "14.0.1.1.0",
    "category": "Animal",
    "website": "https://github.com/OCA/vertical-agriculture",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["bealdav"],
    "license": "AGPL-3",
    "installable": True,
    "summary": "Animal Herd management",
    "depends": [
        "animal_owner",
    ],
    "data": [
        "views/animal.xml",
        "views/herd.xml",
        "views/specie.xml",
        "data/animal_species.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
}
