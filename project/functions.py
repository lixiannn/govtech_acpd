from project.models import Course
import math

def count_gpa(records):
    total_grade_point, total_credit = 0, 0
    for record in records:
        course = Course.query.filter_by(course_id=record.course_id).first()
        total_grade_point += (record.grade_point*course.credit)
        total_credit += course.credit

    gpa = total_grade_point/total_credit
    return gpa

def get_mean_sd(results):
    total_grade_point, standard_deviation = 0, []
    for result in results:
        total_grade_point += result.grade_point

    mean = total_grade_point/len(results)

    for result in results:
        standard_deviation.append((result.grade_point-mean)**2)

    sd = math.sqrt(sum(standard_deviation)/len(results))

    return mean, sd