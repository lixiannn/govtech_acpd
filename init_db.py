from project import db, create_app, models
from werkzeug.security import generate_password_hash

# create all tables
app = create_app()
app.app_context().push()
db.drop_all()
db.create_all() 

# populate data

# create default professor account
new_user = models.User(user_id=1, email='professor@email.com', full_name='Professor', password=generate_password_hash('strongPwd123!', method='sha256'), role='professor')
db.session.add(new_user)
db.session.commit()

# populate some students
new_user = models.User(user_id=2, email='test0@test0.com', full_name='test0', password=generate_password_hash('password', method='sha256'), role='student')
db.session.add(new_user)
db.session.commit()

new_user = models.User(user_id=3, email='test1@test1.com', full_name='test1', password=generate_password_hash('password', method='sha256'), role='student')
db.session.add(new_user)
db.session.commit()

# populate some courses
new_course = models.Course(course_id=1001, course_name='Intro to Python', professor_id=1, credit=3)
db.session.add(new_course)
db.session.commit()

new_course = models.Course(course_id=1002, course_name='Math', professor_id=1, credit=2)
db.session.add(new_course)
db.session.commit()

# populate course result
new_course_result = models.Course_Result(student_id=2, course_id=1001, year_enrolled=2022, grade_point=5.0)
db.session.add(new_course_result)
db.session.commit()

new_course_result = models.Course_Result(student_id=3, course_id=1001, year_enrolled=2022, grade_point=1.0)
db.session.add(new_course_result)
db.session.commit()

new_course_result = models.Course_Result(student_id=2, course_id=1002, year_enrolled=2022, grade_point=3.5)
db.session.add(new_course_result)
db.session.commit()

new_course_result = models.Course_Result(student_id=3, course_id=1002, year_enrolled=2022, grade_point=4.0)
db.session.add(new_course_result)
db.session.commit()