#operater overloading
# print(1+1)
# print('1'+'1')
# print([1,2]+[3,4])

# method overloanding 
# def sum2(a,b):
#     add=a+b
#     return add
# def sum3(a,b,c):
#     add=a+b+c
#     return add

# def sumBetter(a,b,c=0):
#     if(c==0):return sum2(a,b)
#     else:return sum3(a,b,c)

# print(sumBetter(2,3,4))



class User:
    
    def __init__(self,name,mobileNumber,address=""):
        if(address==""):
            self.C1(name,mobileNumber)
        else:
            self.C2(name,mobileNumber,address)
    
    def C1(self,name,mobileNumber):
        self.name = name
        self.mobileNumber = mobileNumber

    def C2(self,name,mobileNumber,address):
        self.name = name
        self.mobileNumber = mobileNumber
        self.address = address
u1 = User("Mayank","9999999")
print(u1.name,u1.mobileNumber)