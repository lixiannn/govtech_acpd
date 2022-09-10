# How to run this program
1. Install dependencies: `pip install -r requirements.txt`
2. Intialise db: `python init_db.py`
3. Depending on your environment,

    If you are on mac, run:

    `export FLASK_APP=project`

    `flask run`

    If you are on windows CMD, run:

    `set FLASK_APP=project`

    `flask run`

    If you are on windows powershell, run: 

    `$env:FLASK_APP = "project"`

    `flask run`

4. Once it is running, navigate to `http://127.0.0.1:5000/{API_ENDPOINT}` for corresponding API.

# API Endpoints available
1. `/login`: allows users to authenticate and login to the application
    - It takes in a `POST` request, with a JSON object as the request body
    - The JSON object should include `email` and `password`
    - For example:
    ```json
        {
            "email": "professor@email.com",
            "password": "strongPwd123!"
        }
2. `/logout`: allows users to logout of the application
    - It takes in a `GET` request
3. `/changePassword`: allows users to change password to their accounts
    - The user must be logged in in order to call this API.
    - It takes in a `POST` request, with a JSON object as the request body
    - The JSON object should include `password` for the new password
    - For example:
    ```json
        {
            "password": "strongPwd123!"
        }
4. `/createAccount`: allows professors to create student accounts with default password as `password`
    - The user must be logged in in order to call this API.
    - The user's role must be a `professor` role.
    - It takes in a `POST` request, with a JSON object as the request body
    - The JSON object should include `email` and `full_name`, which represents the student's email address and full name.
    - For example:
    ```json
        {
            "email": "lixian@test.com",
            "full_name": "Chai Li Xian"
        }
5. `/updateStudentResult`: allows professors to update student's results.
    - The user must be logged in in order to call this API.
    - The user's role must be a `professor` role.
    - It takes in a `POST` request, with a JSON object as the request body
    - The JSON object should include `student_id`, `course_id`, `year_enrolled` and `grade_point`, which represents the student's user id, course id, the year that the student enrolls into this course and the student's grade point for this course.
    - For example:
    ```json
        {
            "student_id": 2,
            "course_id": 1001,
            "year_enrolled": 2022,
            "grade_point": 5.0
        }
6. `/calculateGPA`: allows professors to calculate the GPA of a specified student
    - The user must be logged in in order to call this API.
    - The user's role must be a `professor` role.
    - It takes in a `POST` request, with a JSON object as the request body
    - The JSON object should include `student_id`, which represents the student's user id.
    - For example:
    ```json
        {
            "student_id": 2
        }
7. `/getCoursePerformance`: allows professors to see the mean and standard deviation of a specified course in a particular year
    - The user must be logged in in order to call this API.
    - The user's role must be a `professor` role.
    - It takes in a `POST` request, with a JSON object as the request body
    - The JSON object should include `course_id` and `year_enrolled` which represents the course id and the year that students enroll into this course.
    - For example:
    ```json
        {
            "course_id": 1001,
            "year_enrolled": 2022
        }
8. `/deleteStudent`: allows professors to delete a student record and all the associated data
    - The user must be logged in in order to call this API.
    - The user's role must be a `professor` role.
    - It takes in a `DELETE` request, with a `student_id` as an argument
    - For example: `http://127.0.0.1:5000/deleteStudent/<student_id>`
9. `/viewGPA`: allows students to view their own GPA
    - The user must be logged in in order to call this API.
    - It takes in a `GET` request