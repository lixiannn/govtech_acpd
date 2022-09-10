from flask import Blueprint, request, session
from flask_login import login_user, login_required, current_user, logout_user, fresh_login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/createAccount', methods=['POST'])
@login_required
def createAccount():
    # check if current_user is a prof
    if current_user.role != 'professor':
        return 'Only professors can create account'

    # get info
    account = request.get_json()
    email = account['email']
    full_name = account['full_name']
    password = 'password'
    role = 'student'

    # check if user exists
    user = User.query.filter_by(email=email).first()
    if user:
        return 'User already exists!'

    # insert into db if user does not exist
    new_user = User(email=email, full_name=full_name, password=generate_password_hash(password, method='sha256'), role=role)
    db.session.add(new_user)
    db.session.commit()

    return f'Account created successfully for {full_name}'

@auth.route('/login', methods=['POST'])
def login():
    # get info
    account = request.get_json()
    email = account['email']
    password = account['password']
    remember = True # remember user is logged in

    # check if user exists and check pwd
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return 'Please check your login details & try again!'

    # log user in
    login_user(user, remember=remember)
    return f'Login Successfully as {current_user.full_name}'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout Successfully'

@auth.route('/changePassword', methods=['POST'])
@fresh_login_required
def changePassword():
    # get info
    req = request.get_json()
    password = req['password']

    # update password
    current_user.password = generate_password_hash(password, method='sha256')
    db.session.commit()

    return 'Password is Changed Successfully'