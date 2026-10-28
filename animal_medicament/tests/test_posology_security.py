# Copyright 2026 Escodoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.exceptions import AccessError
from odoo.tests import TransactionCase, tagged
from odoo.tests.common import new_test_user


@tagged("post_install", "-at_install")
class TestPosologySecurity(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = new_test_user(cls.env, login="posology_reader")
        cls.manager = new_test_user(
            cls.env,
            login="posology_manager",
            groups="animal.group_animal_manager",
        )
        cls.product = cls.env["product.product"].create({"name": "Test medicine"})
        cls.posology = cls.env["posology"].create(
            {"description": "Test posology", "product_id": cls.product.id}
        )

    def test_internal_user_can_read(self):
        self.assertEqual(
            self.posology.with_user(self.user).read(["description"])[0]["description"],
            "Test posology",
        )

    def test_internal_user_cannot_modify(self):
        posology = self.posology.with_user(self.user)
        with self.assertRaises(AccessError), self.cr.savepoint():
            posology.write({"meat_time": "10"})
        with self.assertRaises(AccessError), self.cr.savepoint():
            self.env["posology"].with_user(self.user).create(
                {"description": "Unauthorized", "product_id": self.product.id}
            )
        with self.assertRaises(AccessError), self.cr.savepoint():
            posology.unlink()

    def test_animal_manager_can_modify(self):
        posology = (
            self.env["posology"]
            .with_user(self.manager)
            .create({"description": "Manager posology", "product_id": self.product.id})
        )
        posology.write({"meat_time": "10"})
        self.assertEqual(posology.meat_time, "10")
        posology.unlink()
        self.assertFalse(posology.exists())
