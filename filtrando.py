
from data import DATA




def run():
    #testing
    #for i in range (0,len(DATA)):
    #    print(str(i+1)+  ":"+    DATA[i]['name']+    " is a "+DATA[i]['position']+   " from "+    DATA[i]["organization"] )

    platzi_workers= [worker['name'] for worker in DATA if worker['organization']=="Platzi"]

    #adults= [worker['name'] for worker in DATA if worker['age']>18]
    adults=list(filter(lambda worker: worker['age']>18,DATA))
    adults=list(map(lambda worker: worker['name'],DATA))
    old_people = list(map(lambda worker: worker | {"old":worker["age"]>70},DATA))
    #print(old_people)

    for worker in old_people:
        if worker['old']==True:
            print(worker)
        


    

if __name__=="__main__":
    run()
    