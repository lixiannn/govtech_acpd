from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

    def get_id(self):
           return (self.user_id)

class Course_Result(db.Model):
    course_result_id = db.Column(db.Integer, primary_key=True) 
    student_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    year_enrolled = db.Column(db.Integer)
    score = db.Column(db.Integer)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    professor_id = db.Column(db.Integer)
