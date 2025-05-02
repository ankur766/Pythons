'''Create a class Icecream with below attributes:
int - id
int - price
String - name
int - quantityInGms
String - category'''

class Icecream:
    def __init__(self,id,price,name,quantityGms,category):
        self.id=id
        self.price=price
        self.name=name
        self.quantityGms=quantityGms
        self.category=category


class  IcecreamStore:
    def  __init__(self,IcecreamStoreName,IcecreamList):
        self.IcecreamStoreName=IcecreamStoreName
        self.IcecreamList=IcecreamList
    
    @staticmethod
    def findMinimumIcecreamByPrice(arr):
        if not arr:
            return None
        # Find the Icecream with the minimum price
        return min(arr, key=lambda x: x.price)  
         
    @staticmethod 
    def  sortIcecreamByid(arr):
        return sorted(arr,key=lambda x:x.id)
    

n = int(input())
icecreams = []
for i in range(n):
    id = int(input())
    price = int(input())
    name = input()
    quantityInGms = int(input())
    category = input()
    icecreams.append(Icecream(id, price, name, quantityInGms, category))

store_name = input()
store = IcecreamStore(store_name, icecreams)
min_icecream = store.findMinimumIcecreamByPrice(icecreams)
if min_icecream:
        print(min_icecream.id)
        print(min_icecream.price)
        print(min_icecream.name)
        print(min_icecream.quantityInGms)
        print(min_icecream.category)
else:
    print("No Data Found.")
    
sorted_ids = store.sortIcecreamByid(icecreams)
if sorted_ids:
    for id in sorted_ids:
            print(id)
else:
    print("No Data Found.")
        
        