class Movies:
    def __init__(self,moviename,company,gener,budget):
        self.moviename=moviename
        self.company=company
        self.gener=gener
        self.budget=budget
    @staticmethod
    def getmoviesbygener(arr,searchgener):
        result=[]
        for i  in arr:
            if(i.gener.lower()==searchgener.lower()):
                result.append(i)
        return result

arr=[]
for i in range(4):
    moviename=input()
    company=input()
    gener=input()
    budget=int(input())
    store=Movies(moviename,company,gener,budget)
    arr.append(store)

searchgener=input()
result=Movies.getmoviesbygener(arr,searchgener)

for mov in result:
    if(mov.budget>80000000):
        print("high Budget Movies")
    else:print("low Budget")
