class Doctor:
    def __init__(self,doctor_Id,doctor_name,doctor_sep,doctor_consFee):
        self.doctor_Id=doctor_Id
        self.doctor_name=doctor_name
        self.doctor_sep=doctor_sep
        self.doctor_cons=doctor_consFee

# Hospital
class Hospital:
    def __init__(self,doctorDb):
        self.doctor_Db=doctorDb
    
    # searchBydoctor name
    def searchByName(self,name):
        result=[]
        for doctor in self.doctor_Db.values():
            if doctor.doctor_name.lower()==name.lower():
                result.append(doctor)
        if result: return result
        else: return None
            
    def calculationfee(self,sep):
        total=0
        for doctor in self.doctor_Db.values():
            if doctor.doctor_sep.lower()==sep.lower():
                total+=doctor.doctor_cons
        
        print(f'toal is{total}')
        return total




n=int(input())
doctordb={}

for i in range(1,n+1):
    id=int(input())
    name=input()
    sep=input()
    cons=int(input())
    doctor=Doctor(id,name,sep,cons)
    doctordb[i]=doctor

hospital=Hospital(doctordb)

searchNamedoct=input()
result=hospital.searchByName(searchNamedoct)



if result is not None:
    for i in result:
        print(i.doctor_Id)
        print(i.doctor_name)
        print(i.doctor_sep)
        print(i.doctor_cons)
else:print("Not Found")

print("----------output-----------------")
sep=input()
total=hospital.calculationfee(sep)

if total>0:
    print(total)
else: print("No Doctor with the given specialization")

                
    
    