# StudentCourseManagement

A Python-based application designed to manage student information and course enrollment effectively. This system allows for tracking students' GPAs, courses, credit hours, and other academic records.

## Features

- **Student Management**: Create and manage student profiles with name, address, and GPA.
- **Course Management**: Add courses with details such as name, grade, credit hours, and semester.
- **GPA Calculation**: Automatically update and calculate the GPA based on enrolled courses and their grades.
- **Course Enrollment**: Easily enroll students in multiple courses and manage their academic records.

## Classes

### `Student`
- **Attributes**:
  - `name`: Name of the student.
  - `address`: Address of the student.
  - `gpa`: Current GPA of the student.
  - `courses`: List of courses the student is enrolled in.
  - `total_credits`: Total credits earned by the student.

- **Methods**:
  - `addCourse(course)`: Enrolls the student in a new course and updates GPA.
  - `updateGPA()`: Calculates and returns the current GPA based on enrolled courses.

### `Course`
- **Attributes**:
  - `name`: Name of the course.
  - `grade`: Grade received in the course.
  - `hours`: Number of credit hours for the course.
  - `semester`: Semester in which the course was taken.

- **Methods**:
  - `getHours()`: Returns the number of credit hours.
  - `getGrade()`: Returns the grade for the course.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StudentCourseManagement.git

    Navigate to the project directory:

    bash

    cd StudentCourseManagement

    Ensure you have Python installed on your system.

Usage

    Update the new_student.txt file with student and course data in the specified format.
    Run the main script to process the data and manage student records:

    bash

python main.py
