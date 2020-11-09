import unittest
from src import app
paass = app.Pass()

class PasswordTest(unittest.TestCase):
    def test_1_true(self):
        self.assertEqual(paass.ValidPassword("Password1$"), True)
    def test_2_true(self):
        self.assertEqual(paass.ValidPassword("maPasswe2rd**"), True)
    