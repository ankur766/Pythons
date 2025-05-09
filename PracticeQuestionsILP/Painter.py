class Painter:
    def __init__(self,pantid,paintname,paintprice,panttype):
        self.pantid=pantid
        self.paintname=paintname
        self.paintprice=paintprice
        self.panttype=panttype.lower()

    def totalPantingPrice(pantlist,type):
        total=0
        for i in pantlist:
            if i.panttype.lower()==type.lower():
                total+=i.paintprice
        if total:return total
        else:return "No painting Found"
        
    def getpainterMax(pantlist):
        dic={}
        res={}
        
        for i in pantlist:
          
          name = i.paintname.lower()  # consistent key
          dic[name] = dic.get(name, 0) + 1
            
          
          
        maxcount=max(dic.values())
        for name,count in dic.items():
            if count==maxcount:
                res[name]=count
        return res
                
        

n=4
painterList=[]
for i in range(4):
    pantid=input()
    paintname=input()
    paintprice=int(input())
    panttype=input()
    paintStore=Painter(pantid,paintname,paintprice,panttype)
    painterList.append(paintStore)
Type=input()
print(Painter.totalPantingPrice(painterList,Type))
res=Painter.getpainterMax(painterList)
for k,v in res.items():
    print(k,v)
    


    
    
        
        