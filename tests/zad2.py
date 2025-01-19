import unittest
from model.Kamera import Kamera
class TestKamery(unittest.TestCase):
    def test_kamery_1(self):
        self.assertEqual(Kamera(1, "lobby").get_pomieszczenie(), "lobby")