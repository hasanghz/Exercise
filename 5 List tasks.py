import csv
from collections import OrderedDict
with open('D:/python/Exercise/Scores.csv') as f:
    karname=OrderedDict()
    count=0
    list_3up=list()
    moadel=OrderedDict()
    moadel_sorted=OrderedDict()
    x=csv.reader(f)
    moadel_list=list()
    for row in x:
        karname[row[0]]=row[1:]
        y=list(map(int,row[1:]))
        moadel[row[0]]=sum(y)
        moadel_sorted=sorted(moadel.items(),key=lambda item:item[1])
#Task 1 :
    print('''Task 1 is : 
          


          %s''' %moadel)

#Task 2 :
    print('Task 2 is : ')
    for u in moadel_sorted:
        print(u)
    for t in moadel_sorted:
        if count>=(len(moadel_sorted)-3):
            list_3up.append(t)

        
#Task 3:          
        count+=1
    print('''Task 3 is : 
    ''',list_3up)
    for p in moadel_sorted:
        moadel_list.append(p)
#Task 4:
    print('Task 4 is : ')

    for q in range (3):
        print(moadel_list[q][1])
#Task 5 :
    print('Task 5 is : ')
    print(sum(moadel.values())/len(moadel))
    
