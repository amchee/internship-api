from app.db import db

class InternModel(db.Model):
    __tablename__ = 'interns'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)
    description = db.Column(db.String(255))  # new field for internship description

    university = db.relationship('UniversityModel')

    def __init__(self, name, university_id, description=None):
        self.name = name
        self.university_id = university_id
        self.description = description

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
