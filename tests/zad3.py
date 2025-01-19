import unittest
from model.Dao import get_lista_kamer
class TestDao(unittest.TestCase):
    def test_kamery_1(self):
        self.assertEqual(get_lista_kamer().__getitem__(2).get_pomieszczenie(), "magazyn")