class NavalVessel:
    def __init__(self,vessid,vessname,noofvoyageplanne,noofcompleted,purpose):
        self.vessid=vessid
        self.vessname=vessname
        self.noofvoyageplanne=noofvoyageplanne
        self.noofcompleted=noofcompleted
        self.purpose=purpose
    @staticmethod
    def findAvgVoyagesByPct(arr,perct):
        sum=0
        count=0
        for i in arr:
            sum=0
            count=0
            pt=(i.noofvoyageplanne*100)//i.noofcompleted
            if(pt>=perct):
               sum+=i.noofcompleted 
               count+=1
        avg=sum//count
        return avg
    @staticmethod
    def findVesselByGrade(arr,purpose):
        res=[]
        for i in arr:
            if(i.purpose.lower()==purpose.lower()):
                res.append(i)
        return res

arr=[]
for i in range(4):
    vessid=int(input())
    
    vessname=input()
    noofvoyageplanne=int(input())
    noofcompleted=int(input())
    purpose=input()

perct=int(input())
pur=input()
total=NavalVessel.findAvgVoyagesByPct(arr,perct)
res=NavalVessel.findVesselByGrade(arr,pur)
print(total)
for i in res:
    print(i.vessid)
      
    
    
    
                
        
            
        
        