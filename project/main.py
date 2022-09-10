from flask import Blueprint, request
from project.auth import login
from project.functions import count_gpa, get_mean_sd
from project.models import Course_Result, User
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
    grade_point = req['grade_point'] # [0.0-5.0]

    if grade_point < 0 or grade_point > 5.0:
        return "Grade Point should be in the range of 0.0-5.0 inclusive."

    # check if record already exists
    record = Course_Result.query.filter_by(student_id=student_id, course_id=course_id, year_enrolled=year_enrolled ).first()
    if record:
        record.grade_point = grade_point # update grade_point
        db.session.commit()
    else:
        # else, create new entry
        new_record = Course_Result(student_id=student_id, course_id=course_id, year_enrolled=year_enrolled, grade_point=grade_point)
        db.session.add(new_record)
        db.session.commit()

    return 'Result updated'

# for professors to calculate GPA of a specified student
@main.route('/calculateGPA', methods=['POST'])
@login_required
def calculateGPA():
    # check if current_user is prof
    # only prof can view gpa of any specified student
    if current_user.role != 'professor':
        return 'Unauthorized. Only professors can view GPA of specified student'

    # get info
    req = request.get_json()
    student_id = req['student_id']

    # query for student's course result
    records = Course_Result.query.filter_by(student_id=student_id).all()
    if records:
        gpa = count_gpa(records)
        user = User.query.filter_by(user_id=student_id).first()
        return f'GPA of {user.full_name} is: {gpa}'
    else:
        return 'No course result records. Please add them first.'

@main.route('/getCoursePerformance', methods=['POST'])
@login_required
def getCoursePerformance():
    # check if current_user is prof
    if current_user.role != 'professor':
        return 'Unauthorized. Only professors can view course performance'
    
    # get info
    req = request.get_json()
    course_id = req['course_id']
    year_enrolled = req['year_enrolled']

    # query for course results
    results = Course_Result.query.filter_by(course_id=course_id, year_enrolled=year_enrolled).all()
    if results:
        mean, sd = get_mean_sd(results)
        return f'Mean and Standard Deviation for Course {course_id}: {mean}, {sd}'
    else:
        return 'No records found.'

@main.route('/deleteStudent/<student_id>', methods=['DELETE'])
@login_required
def deleteStudent(student_id):
    # check if current_user is prof
    if current_user.role != 'professor':
        return 'Unauthorized. Only professors can delete student record'

    # get info
    user = User.query.filter_by(user_id=student_id).first()
    name = user.full_name

    # delete student's course results
    Course_Result.query.filter_by(student_id=student_id).delete()
    # delete student record
    User.query.filter_by(user_id=student_id).delete()
    db.session.commit()
   
    return f'Student Record for {name} deleted'

# for student to view his/her own GPA
@main.route('/viewGPA')
@login_required
def viewGPA():
    # query for student's course result
    records = Course_Result.query.filter_by(student_id=current_user.user_id).all()
    if records:
        gpa = count_gpa(records)
        return f'GPA of {current_user.full_name} is: {gpa}'
    else:
        return 'No course result records.'