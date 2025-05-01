class Student:
    __numberOfStudent=0
    __schoolName="Maps"
    isplusMember=True
    def __init__(self,name,rollNumber,marks):
        self.name=name
        self.rollnumber=rollNumber
        self.__marks=marks
        Student.__numberOfStudent+=1
    #getter
    def getmarks(self):
        return self.__marks
    #setter
    def setmarks(self,marks):
        self.__marks=marks
    @staticmethod
    def getNoOfStudent():
        return Student.__numberOfStudent
    @staticmethod
    def getSchoolName():
        return Student.__schoolName
    @staticmethod
    def sentmail():
        print(  "School Name chnage")
    
    
# creating object
S1=Student("Ankur",20,85)
print(S1.name)
print(S1.rollnumber)
print(S1.getmarks())

print(Student.getSchoolName())
Student.sentmail()

S1.setmarks(99)
print(S1.name)
print(S1.rollnumber)
print(S1.getmarks())

print(Student.getSchoolName())
Student.sentmail()
    