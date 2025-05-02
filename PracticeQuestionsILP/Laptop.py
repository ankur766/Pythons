class Laptop:
    def __init__(self,id,brand,ostype,price,rating):
        self.id=id
        self.brand=brand
        self.ostype=ostype
        self.price=price
        self.rating=rating

    @staticmethod
    def countByBrand(arr,brand):
        totalcount=0
        for i in arr:
            if(i.rating>3 and i.brand.lower()==brand.lower()):
                totalcount+=1
        return totalcount       
            
    

    @staticmethod
    def searchbyType(arr,type):
        result={}
        for i in arr:
            if type.lower() in i.ostype.lower():
                result[i.id]=i.rating
    
        result=dict(sorted(result.items(),reverse=True))
        return result

n=4
arr=[]
for i in range(1,n+1):
    id=int(input())
    brand=input()
    ostype=input()
    price=float(input())
    rating=int(input())
    laptop=Laptop(id,brand,ostype,price,rating)
    arr.append(laptop)


searchbrand=input()
totalcount=Laptop.countByBrand(arr,searchbrand)
print(totalcount)
searchos=input()
result=Laptop.searchbyType(arr,searchos)
for k,v in result.items():
    print(k)
    print(v)

            
             
             
    