class Book:
    def __init__(self,bookid,bookname,nameofauthor):
        self.bookid=bookid
        self.bookname=bookname
        self.nameofauthor=nameofauthor
        
    @staticmethod
    def countbook(arr):
        arrset=set()
        fildic={}
        author=[ar.nameofauthor.upper() for ar in arr]
        for ar in author:
            arrset.add(ar)
        for s in arrset:
            fildic[s]=author.count(s)
        return fildic
    
class Address:
    def __init__(self,street,area,city,state,zip):
        self.street=street
        self.area=area
        self.city=city
        self.state=state
        self.zip=zip
    
    
    
    
    @staticmethod
    def areaofBook(diclib,searchcity):
        storebook=[]
        for k,v in diclib.items():
            if searchcity.lower() in v.city.lower():
                storebook.append(k.bookname)
        return storebook
               
        
        
            
        


n= int(input())
booklist=[]
diclib={}

for i in range(n):
    bookid=int(input())
    bookname=input()
    nameofAuthor=input().upper()
    book=Book(bookid,bookname,nameofAuthor)
    booklist.append(book)


    street=input()
    area=input()
    city=input()
    state=input()
    zip=int(input())
    storearea=Address(street,area,city,state,zip)
    diclib[book]=storearea
    
result=Book.countbook(booklist)
for k,v in result.items():
    print(k,v)
searchcity=input()
res=Address.areaofBook(diclib,searchcity)
for k,v in result.items():
    print(k,v)
for l in res:
    print(l)
    

    
    
    
    
    
