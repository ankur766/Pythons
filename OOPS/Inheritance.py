class user:
    def __init__(self,name,id,age,passcode):
        self.name=name
        self.id=id
        self.age=age
        self.passcode=passcode
        
    
    def login(self):
        return 'succesfully Login'
    
    
    def logout(self):
        return "logout"
    
    
class Student(user):
    def __init__(self,name,id,age,passcode,rollNumber,marks):
        super().__init__(name,id,age,passcode)
        self.rollNumber=rollNumber
        self.marks=marks
    def login(self):
        print("otp sent")
        print(super().login())

s1=Student("Ankur",272,24,12345,7666,82)
s1.login()
print(f'Name is:{s1.name} mark:{s1.marks} age:{s1.age} ')

print(s1.logout())