from flask import Blueprint, request
from project.models import Course_Result
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/updateStudentResult', methods=['POST'])
@login_required
def updateStudentResult():
    # check if current user is a prof
    if current_user.role != 'professor':
        return 'Unauthorized. Only professors can update results.'

    # get info
    req = request.get_json()
    student_id = req['student_id']
    course_id = req['course_id']
    year_enrolled = req['year_enrolled']
    score = req['score']

    # check if record already exists
    record = Course_Result.query.filter_by(student_id=student_id, course_id=course_id, year_enrolled=year_enrolled ).first()
    if record:
        record.score = score # update score
    else:
        # else, create new entry
        new_record = Course_Result(student_id=student_id, course_id=course_id, year_enrolled=year_enrolled, score=score)
        db.session.add(new_record)
        db.session.commit()

    return 'Result updated'

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