from . import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

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

