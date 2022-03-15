import unittest
from app import app


class TestApp(unittest.TestCase):

    def test_given_no_user_logged_in_get_login_returns_200(self):
        with app.test_client() as client:
            response = client.get('/user/login')
            assert response._status_code == 200

    def test_given_no_user_logged_in_get_user_new_returns_200(self):
        with app.test_client() as client:
            response = client.get('/user/new')
            assert response.status_code == 200

    def test_given_no_user_logged_in_get_user_new_returns_register_data(self):
        with app.test_client() as client:
            response = client.get('/user/new')
            assert b"<h4>Register</h4>" in response.data


