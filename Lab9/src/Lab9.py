from student import Student
from course import Course
'''
Created on May 1, 2022

@author: michaelmordec
'''
def main():
    file = open("new_student.txt","r")
    students = []
    student = Student(1,2)
    for rawline in file:
        line = rawline.strip()
        #print(line)
        field = line.split()
        if(len(field)==2):
            student = Student(line,"address")
            students.append(student)
        elif(len(field)==5):
            new_course = Course(field[0] + " " + field[1],field[2],field[3],field[4])
            student.addCourse(new_course)        
    file.close()
    
    for student in students:
        print(student)
main()