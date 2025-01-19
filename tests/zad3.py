import unittest
from parameterized import parameterized
from model.Dao import Dao
from model.Kamera import Kamera


class TestDao(unittest.TestCase):
    def setUp(self):
        self.dao = Dao
    def test_dao_1(self):
        self.dao.update_kamera(Dao)
        self.assertEqual(self.dao.get_kamery()[-1].get_pomieszczenie(), "korytarz")
        self.assertEqual(self.dao.get_kamery()[-1].get_kod(), "1")

    # @parameterized.expand([
    #     (1, "korytarz", ""),
    #     ("lobby", 3, "3lobby"),
    # ])
    # def test_dao_parameterized_1(self, id, nazwa, expected_result):
    #     self.dao.update_kamera(Kamera(id, nazwa))
    #     result = self.dao.get_kamera(
    #     self.assertEqual(result, expected_result)