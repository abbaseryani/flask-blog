import unittest
from flask import request
from flask import Flask
import flaskblog

app = flaskblog.create_app()


class MyAppCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.Testing = True
        self.app.WTF_CSRF_ENABLED = False

    def test_config(self):
        self.assert_(app.config["DEBUG"] is True)

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertIn(b'About Page', response.data)
        assert response.status_code == 200

    def test_home_page(self):
        response = self.app.get('/')
        self.assertIn(b'hello world', response.data)
        assert response.status_code == 200

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertIn(b'password', response.data)
        assert response.status_code == 200

    # Ensure users can login with correct credentials
    def test_login_logout(self):
        rv = self.logout('adminx', 'default')
        self.assertIn(b'Login unsuccessful', rv.data)
        rv = self.login('abbaseryani@gmail.com', '111')
        self.assertIn(b'You were logged in', rv.data)

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
