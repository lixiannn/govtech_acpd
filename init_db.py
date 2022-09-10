from project import db, create_app, models
from werkzeug.security import generate_password_hash

# create all tables
app = create_app()
app.app_context().push()
db.drop_all()
db.create_all() 

# create default professor account
new_user = models.User(email='professor@email.com', full_name='Professor', password=generate_password_hash('strongPwd123!', method='sha256'), role='professor')
db.session.add(new_user)
db.session.commit()

# populate some courses
new_course = models.Course(course_id=1001, course_name='Intro to Python', professor_id=1, credit=3)
db.session.add(new_course)
db.session.commit()

new_course = models.Course(course_id=1002, course_name='Math', professor_id=1, credit=2)
db.session.add(new_course)
db.session.commit()