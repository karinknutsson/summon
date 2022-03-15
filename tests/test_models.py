import unittest
from models import User


class TestApp(unittest.TestCase):

    def test_given_password_and_password_hash_match_return_true(self):
        user = User()
        user.password = "foo"
        self.assertTrue(user.check_password("foo"))

    def test_given_password_and_password_hash_dont_match_return_false(self):
        user = User()
        user.password = "foo"
        self.assertFalse(user.check_password("bar"))

