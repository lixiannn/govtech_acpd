from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

@main.route('/updateStudentResult')
def updateStudentResult():
    return 'Update Student Result'

# for professors to calculate GPA of a specified student
@main.route('/calculateGPA')
def calculateGPA():
    return 'GPA'

@main.route('/getCoursePerformance')
def getCoursePerformance():
    return 'Course Performance'

@main.route('/deleteStudent')
def deleteStudent():
    return 'deleteStudent'

# for student to view his/her own GPA
@main.route('/viewGPA')
def viewGPA():
    return 'GPA'