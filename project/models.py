from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __table__name = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

    def get_id(self):
           return (self.user_id)

class Course(db.Model):
    __table__name = 'course'
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    professor_id = db.Column(db.Integer)
    credit = db.Column(db.Integer)

class Course_Result(db.Model):
    course_result_id = db.Column(db.Integer, primary_key=True) 
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    year_enrolled = db.Column(db.Integer)
    grade_point = db.Column(db.Integer)

