class Employee:
    def __init__(self,emid,name,role,age):
        self.emid=emid
        self.name=name
        self.role=role.lower()
        self.age=age
        
    
class Oraganation:
    
    def __init__(self,emlist,dic):
        self.emlist=emlist
        self.dic=dic
    @staticmethod
    def findeligibility(emlist,dic):
        res={}
        
        for i in emlist:
           
            if i.role in dic.keys(): 
              if i.age==dic[i.role]:
                res[i.emid]="Eligible"
              elif i.age<dic[i.role]:
                res[i.emid]=f'Not Eligible :{dic[i.role] -i.age}'
              elif i.age>dic[i.role]:
                res[i.emid]=f'Over Eligible :{i.age-dic[i.role] }'
            
        return res

# main
n=4
emplist=[]

roldic={}

for i in range(n):
    empid=int(input())
    name=input()
    role=input().lower()
    exp=int(input())
    empStore=Employee(empid,name,role,exp)
    emplist.append(empStore)

for i in range(3):
    role=input().lower()
    exp=int(input())
    roldic[role]=exp
res= Oraganation.findeligibility(emplist,roldic)
for k,v in res.items():
    print(k,v)
    
    

                
 