from collections import OrderedDict
with open('d:\\python\\exercise\\exercise\\sales_data.txt') as myfile:
    dic={}
    for line in iter(myfile.readline,''):
        word=line.strip().split(',')
        try:
            word[1]=int(word[1])
            dic[word[0]]=word[1]
        except ValueError:
            continue
        
with open('d:\\python\\exercise\exercise\Results_project4.txt','wt') as result:
    sum=0
    x=0
    mean=0
    lowest=0
    lowest_2=0
    highest=0
    lis_values=dic.values()
    for n in lis_values:
        
        sum+=n
        
        mean=sum/len(dic)
        lowest=min(dic.values())
        highest=max(dic.values())

    
    
    result.write(f'The number of valid values is : {len(dic)} \nThe sum is : {sum} \nThe mean is : {mean}\nThe lowest is : {lowest}\nThe highest is : {highest} ')
    print(dic, '    ',lis_values)