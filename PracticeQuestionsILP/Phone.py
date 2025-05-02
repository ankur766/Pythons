class Movies:
    def __init__(self,phnid,os,brand,price):
        self.phnid=phnid
        self.os=os
        self.brand=brand
        self.price=price
    @staticmethod
    def getpricebybrand(arr,sechbrand):
        sum=0
        for i in arr:
            if(i.brand.lower()==sechbrand.lower()):
                sum+=i.price
        return sum
    @staticmethod
    def getphoneidbyOs(arr,byos):
        result=[]
        for i in arr:
            if(i.os.lower()==byos.lower()):
                result.append(i)
        return result

arr=[]
for i in range(4):
    phnid=int(input())
    os=input()
    brand=input()
    price=int(input())
    store=Movies(phnid,os,brand,price)
    arr.append(store)

sechbrand=input()
byos=input()
total=Movies.getpricebybrand(arr,sechbrand)
byos=Movies.getphoneidbyOs(arr,byos)
if total>0:
    print(total)
else:print("No")
for i in byos:
    print(i.phnid)

    
     
        
        
