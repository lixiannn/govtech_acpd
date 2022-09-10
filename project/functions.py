from project.models import Course

def count_gpa(records):
    total_grade_point, total_credit = 0, 0
    for record in records:
        course = Course.query.filter_by(course_id=record.course_id).first()
        total_grade_point += (record.grade_point*course.credit)
        total_credit += course.credit

    gpa = total_grade_point/total_credit
    return gpa