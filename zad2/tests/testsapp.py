import unittest
from src import app
paass = app.Pass()

class PasswordTest(unittest.TestCase):
    def test_1_true(self):
        self.assertEqual(paass.ValidPassword("Password1$"), True)

    def test_2_true(self):
        self.assertEqual(paass.ValidPassword("maPasswe2rd**"), True)

    def test_3_false_no_special(self):
        self.assertEqual(paass.ValidPassword("PppPaAcc2dasx"), False)

    def test_4_false_no_upper(self):
        self.assertEqual(paass.ValidPassword("%^*sdasfage2aegse"), False)

    def test_5_false_no_number(self):
        self.assertEqual(paass.ValidPassword("%^(macgeFEWdaf"), False)

    def test_6_false_short(self):
        self.assertEqual(paass.ValidPassword("%*4M"), False)

    def test_exception_type(self):
        with self.assertRaises(TypeError):
            paass.ValidPassword(1)

    def test_exception_space(self):
        with self.assertRaises(ValueError):
            paass.ValidPassword("Hnad^&7dkaf da")


