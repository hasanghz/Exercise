def menu():
    func = -4
    while func<0 or func>9:
        func=int(input('Please enter a number between 0 and 9 the function you want : '))
    
    print('1-Add a value to the list.')
    print('2-Add a value to special location')
    print('3-Omit a member of the list')
    print('4-Sort the list members')
    print('5-Reverse the members')
    print('6-Count the number of repetitions of a member')
    print('7-Find a location of a value')
    print('8-Press 0 to exit')
    return func
n=input('Please enter the members of the list with a space.')
list1=[]
list1=n.split()
while 1:
    x=menu()
    if x==1:
        y=input('Please enter the value : ')
        list1.append(y)
        print('New lest is : ',list1)
    elif x==2 :
         list2=[]
         y=input('Please enter the location and the value : ')
         list2=y.split()
         list1.insert(int(list2[0]),(int(list1[1])))
         print('New list is : ', list1)
    elif x==3 :
        y=input('Please enter the value : ')
        if y in list1:
            list1.remove(y)
            print(list1)
        else:
            print('The value is not existed')
    elif x==4 :
        list1.sort()
        print(list1)
    elif x==5 :
        list1.sort(reverse=True)
    elif x==6:
        y=input('Please enter the value that you want to be chacked : ')
        print(list1.count(y))
    elif x==7 :
        y=input('Please enter the value th find its location : ')
        print('The location is : %s' %list1.index(y))
    elif x==0 :
        break
