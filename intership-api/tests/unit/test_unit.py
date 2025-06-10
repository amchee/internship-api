import unittest
from app.models.user import UserModel
from app.models.intern import InternModel
from app.models.university import UniversityModel

class TestUserModel(unittest.TestCase):
    def test_create_user(self):
        user = UserModel(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpass')

class TestUniversityModel(unittest.TestCase):
    def test_create_university(self):
        university = UniversityModel(name='Test University')
        self.assertEqual(university.name, 'Test University')

class TestInternModel(unittest.TestCase):
    def test_create_intern(self):
        intern = InternModel(name='Test Intern', university_id=1, description='A test internship')
        self.assertEqual(intern.name, 'Test Intern')
        self.assertEqual(intern.university_id, 1)
        self.assertEqual(intern.description, 'A test internship')

if __name__ == '__main__':
    unittest.main()
