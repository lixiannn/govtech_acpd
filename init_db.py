from project import db, create_app, models
from werkzeug.security import generate_password_hash

# create all tables
app = create_app()
app.app_context().push()
db.create_all() 

# create default professor account
new_user = models.User(email='professor@email.com', full_name='Professor', password=generate_password_hash('strongPwd123!', method='sha256'), role='professor')
db.session.add(new_user)
db.session.commit()
