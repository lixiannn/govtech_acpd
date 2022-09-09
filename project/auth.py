from flask import Blueprint, request
from flask_login import login_required

from . import db

auth = Blueprint('auth', __name__)

@auth.route('/createAccount', methods=['POST'])
@login_required
def createAccount():
    return 'Account created successfully'

@auth.route('/login', methods=['POST'])
def login():
    return 'Login Successfully'

@auth.route('/logout')
@login_required
def logout():
    return 'Logout Successfully'