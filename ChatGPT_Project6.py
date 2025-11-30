dic={}

cost=[]
with open('d:\\python\\exercise\\exercise\\pr5.txt') as file:
    for line in iter(file.readline,''):
        
        lis=line.strip().split(',')
        for i in range(len(lis)):
            try:
                lis[i]=lis[i].strip()
                lis[i]=int(lis[i])  
            except:
                continue
        print(lis)
        for i in dic:
            print(i)
            if i==lis[0]:
                dic[lis[0]]=dic[lis[0]]+(lis[2]*lis[3])
                print('yes')
            else:
                dic[lis[0]]=(lis[2]*lis[3])
                print('no')       
       
        cost.append(lis[2]*lis[3])
     
print(cost,dic)
        