def readlist():
    s1=input('Please enter the first list : ')
    s2=input('Pleae enther the second list : ')
    list1=s1.split()
    list2=s2.split()
    return (list1,list2)
def share(x,y):
    list3=[]
    for i in x:
        if i in y:
            list3.append(i)
    print(list3)
def union(x,y):
    list3=[]
    for i in x:
        list3.append(i)
    for i in y:
        if i not in x:
            list3.append(i)
    print(list3)
def difference(x,y):
    list3=[]
    for i in x:
        if i not in y:
            list3.append(i)
    for i in y:
        if i not in x:
            list3.append(i)
    print(list3)

list1,list2=readlist()

share(list1,list2)

union(list1,list2)

difference(list1,list2)