import unittest
import json
from app import create_app, db

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_full_workflow(self):
        # Register user
        self.client.post('/register', json={'username': 'sysuser', 'password': '1234'})

        # Login
        res = self.client.post('/login', json={'username': 'sysuser', 'password': '1234'})
        token = res.get_json()['access_token']
        headers = {'Authorization': f'Bearer {token}'}

        # Create university
        res_uni = self.client.post('/universities', headers=headers, json={'name': 'SysTest University'})
        uni_id = res_uni.get_json()['id']

        # Create intern
        res_intern = self.client.post('/interns', headers=headers, json={
            'name': 'SysTest Intern',
            'university_id': uni_id,
            'description': 'End-to-end intern'
        })
        self.assertEqual(res_intern.status_code, 201)
        self.assertIn('Intern created', res_intern.get_json()['message'])

if __name__ == '__main__':
    unittest.main()
