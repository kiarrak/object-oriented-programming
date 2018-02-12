def averageGrade(grades):
    sum =0
    for i in grades:
        sum +=i
    return 1.0*sum/len(grades)
class Teacher():
    def __init__(self,lastName,subject):
        self.lastName=lastName
        self.subject=subject
    def printName(self):
        return self.lastName
    
class Student():
    def __init__(self, firstName, lastName, middleInitial, teacher):
        self.firstName=firstName
        self.lastName=lastName
        self.middleInitial=middleInitial
        self.grades=[]
        self.teacher=teacher
    def addGrade(self, grade):
        self.grades.append(grade)
    def getGrade(self):
        sum =0
        for i in self.grades:
            sum +=i
        return 1.0*sum/len(self.grades)
    def printName(self):
        return self.firstName +" " + self.middleInitial + " " + self.lastName
    def setLastName(self,newLastName):
        self.lastName=newLastName
    def printTeachersName(self):
        return self.teacher.printName()
