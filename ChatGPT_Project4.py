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
    mean=0
    lowest=0
    highest=0
    lis_values=dic.values()
    for n in lis_values:
        sum+=n
        mean=sum/len(dic)
        if lowest>n:
            lowest=n
        if n> highest:
            highest=n

    
    
    result.write(f'The number of valid values is : {len(dic)} \nThe sum is : {sum} \nThe mean is : {mean}\nThe lowest is : {lowest}\n The highest is : {highest} ')
    print(dic, '    ',lis_values)