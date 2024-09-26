class Course:
    '''
    classdocs
    '''
    def __init__(self, name, grade, hours, semester):
        '''
        Constructor
        '''
        self.__name = name
        self.__grade = grade
        self.__hours = int(hours)
        self.__semester = semester
    
    def __str__(self):
        return self.__name + " " + str(self.__semester)
    
    def getHours(self):
        return self.__hours
    
    def getGrade(self):
        return self.__grade