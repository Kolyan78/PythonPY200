import unittest

from task import Glass


class TestCase(unittest.TestCase):
    # todo check get_material method

    def test_get_material(self):
        material = "paper"
        glass = Glass(material=material)
        self.assertEqual(material, glass.get_material(),
                         msg="Метод get_material должен возвращать материал стакана.")
