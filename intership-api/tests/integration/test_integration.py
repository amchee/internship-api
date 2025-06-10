import unittest
from main import create_app
from app.db import db
from app.models.intern import InternModel
from app.models.university import UniversityModel

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            uni = UniversityModel(name='Integration University')
            db.session.add(uni)
            db.session.commit()

            intern = InternModel(name='Intern A', university_id=uni.id, description='Integration test')
            db.session.add(intern)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_intern_linked_to_university(self):
        with self.app.app_context():
            intern = InternModel.query.filter_by(name='Intern A').first()
            university = UniversityModel.query.get(intern.university_id)
            self.assertIsNotNone(intern)
            self.assertEqual(university.name, 'Integration University')

if __name__ == '__main__':
    unittest.main()
