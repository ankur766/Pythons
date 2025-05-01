class Grandfather:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        return f'Name: {self.name}, Age: {self.age}'
        
    def speak(self):
        return 'Grandfather speaks wisely.'
class Child1(Grandfather):
    def __init__(self,name,age,hobby):
        super().__init__(name,age)
        self.hobby=hobby
    def showHobby(self):
        return f'Hobby is :{self.hobby}'
    def speak(self):
        return 'child1 is speak good'
    def show_details(self):
            return f'Name: {self.name}, Age: {self.age}'
    
    
class Child2(Grandfather):
    def __init__(self,name,age,favsub):
        super().__init__(name,age)
        self.favsub=favsub
        
    def favsubject(self):
        return f'Hobby is :{self.favsub}'
    
    def speak(self):
        return 'child1 is speak good'
    
    
    
child1_obj = Child1('Alice', 20, 'Painting')
child2_obj = Child2('Bob', 22, 'Mathematics')
print(child1_obj.show_details())
print(child1_obj.showHobby())
print(child1_obj.speak())

print(child2_obj.show_details())

print(child2_obj.favsubject())
print(child2_obj.speak())
