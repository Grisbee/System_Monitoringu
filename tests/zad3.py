import unittest
from parameterized import parameterized
from model.Dao import Dao
from model.Kamera import Kamera


class TestDao(unittest.TestCase):
    def setUp(self):
        self.dao = Dao()
    def test_dao_1(self):
        self.dao.update_kamera(Kamera(30, "salon"))
        self.assertEqual(self.dao.get_kamery()[-1].get_pomieszczenie(), "salon")
        self.assertEqual(self.dao.get_kamery()[-1].get_kod(), 30)

    @parameterized.expand([
        (10, "korytarz", 30, "salon"),
        (120, "lobby", 30, "salon"),
    ])
    def test_dao_parameterized(self, id, nazwa, expected_result1, expected_result2):
        self.dao.update_kamera(Kamera(id, nazwa))
        kamera = self.dao.get_kamery()[-1]
        self.dao.delete_kamera(kamera)
        result1 = self.dao.get_kamery()[-1].get_kod()
        result2 = self.dao.get_kamery()[-1].get_pomieszczenie()
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)