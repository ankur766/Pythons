class Grandfather:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showdetails(self):
        return f'Nmae:{self.name}, Age: {self.age}'
    def speak(self):
        return "Great Man"

class Father(Grandfather):
    def __init__(self,name,age,occupation):
        super().__init__(name,age)
        self.occupation=occupation
    def show_occupation(self):
        return f'occupation: {self.occupation}'
    def speak(self):
        return 'sweet'
    
    #creating Object
fatherObj=Father('Ankur',50,'Engineer')
print(fatherObj.showdetails())
print(fatherObj.speak())
print(fatherObj.show_occupation())
    