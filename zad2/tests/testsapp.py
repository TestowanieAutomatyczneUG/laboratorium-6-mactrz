import unittest
from src import app
Pass = app.Pass

class PasswordTest(unittest.TestCase):
    def test_1_true(self):
        self.assertEqual(Pass.ValidPassword("Password2&"), True)