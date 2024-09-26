'''
@author: michaelmordec
'''
#this is a class definition
class Student:
    '''
    classdocs
    '''
    #initializer method is automatically called when an instance of a Student is created
    #self refers to the Student object
    #there can be only one init per class
    def __init__(self, name, address):
        self.__name = name
        self.__gpa = 0
        self.__courses = []  #make an empty list for the student's courses
        self.__address = address
        self.__total_credits = 0
        self.__past_courses = []       
        
    #returns the Student objects state as a string
    def __str__(self):
        s = self.__name 
        s += "\nGPA: " 
        s += str(format(self.__gpa, ",.2f")) 
        s += "\nTotal credits: " 
        s += str(format(self.__total_credits, ",.0f")) 
        s += "\nCourses taken:\n"
        for c in self.__courses:
            s += str(c) + "\n"
        return s
    def addCourse(self, new_course):
        self.__courses.append(new_course)
        self.__gpa = self.updateGPA()
        self.__total_credits += new_course.getHours()
        
    def updateGPA(self):
        total_hours = 0
        total_points = 0
        for course in self.__courses:
            total_hours += course.getHours()  #course.hours won't work because hours is private
            if course.getGrade() == "A":
                total_points += course.getHours() * 4.0
            elif course.getGrade() == "B":
                total_points += course.getHours() * 3.0
            elif course.getGrade() == "C":
                total_points += course.getHours() * 2.0
            elif course.getGrade() == "D":
                total_points += course.getHours() * 1.0
        return total_points / total_hours
  
        
    
    
    
    
    
    
    
    
    
    
