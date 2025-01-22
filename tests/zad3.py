import unittest
from parameterized import parameterized
from model.Dao import Dao
from model.Kamera import Kamera
from model.Czujnik import Czujnik


def ordered_test_loader():
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = lambda x, y: {
        'test_dao_1': 0,
        'test_dao_kamery_parameterized': 1,
        'test_dao_czujniki_parameterized': 2
    }[x] - {
        'test_dao_1': 0,
        'test_dao_kamery_parameterized': 1,
        'test_dao_czujniki_parameterized': 2
    }[y]
    return loader


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
    def test_dao_kamery_parameterized(self, id, nazwa, expected_result1, expected_result2):
        self.dao.update_kamera(Kamera(id, nazwa))
        kamera = self.dao.get_kamery()[-1]
        self.dao.delete_kamera(kamera)
        result1 = self.dao.get_kamery()[-1].get_kod()
        result2 = self.dao.get_kamery()[-1].get_pomieszczenie()
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)

    @parameterized.expand([
        (7, "zsyp_na_kartofle", "wykrywacz_gazu", 3, "zsyp_na_kartofle", "wykrywacz_dymu"),
        (5, "dungeon", "czujnik_czucia", 3, "zsyp_na_kartofle", "wykrywacz_dymu"),
    ])
    def test_dao_czujniki_parameterized(self, czujnik_id, nazwa, typ, expected_result1, expected_result2, expected_result3):
        self.dao.update_czujnik(Czujnik(czujnik_id, nazwa, typ))
        czujnik = self.dao.get_czujniki()[-1]
        print("testxxx")
        print(czujnik)
        self.dao.delete_czujnik(czujnik)
        result1 = self.dao.get_czujniki()[-1].get_kod()
        result2 = self.dao.get_czujniki()[-1].get_pomieszczenie()
        result3 = self.dao.get_czujniki()[-1].get_rodzaj_czujnika()
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)


if __name__ == '__main__':
    suite = ordered_test_loader().loadTestsFromTestCase(TestDao)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)