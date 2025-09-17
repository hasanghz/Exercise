from collections import OrderedDict

    
def add(telbook):          
    name=input('Please Enter the name of the contact that you want to add : ')
    number=int(input('Please enter the number of the contact : '))
    telbook[name]=number
    print(telbook)

def delete(telbook):
    name=input('Please enter the name of the contact that you want to delete : ')
    del telbook[name]
    print(telbook)

def search(telbook):
    name=input('Please enter the contact you want to find : ')
    print('The contact number is : ',telbook.setdefault(name,'The contact doesnt exist. '))

def change_number(telbook):
    name=input('Please enter the contact taht you want to change the number : ')
    new_num=int(input('Please enter the new number : '))
    contact={}
    contact[name]=new_num
    telbook.update(contact)
    print(telbook)

def change_name(telbook):
    number=(input('Please enter the number that you want to change its name : '))
    new_name=input('Please enter the new name : ')
    telbook[new_name]=number
    
    for t in telbook:
        
        
        if number == telbook[t]:
            del telbook[t]
            break
    print(telbook)



    
    

def show_all_contacts(telbook):
    for i in telbook:
        print(i,' :' ,telbook[i])



n=int(input('Please enter the number of the contact : '))
telbook=OrderedDict()
for i in range (n):
    name=input('Please enter the contact name : ')
    number=input('Please enter the contact number : ')
    telbook[name]=number


while 1:


    print('1.Add a contact.')
    print('2.Delete a contact.')
    print('3.Search a contact.')
    print('4.Change a phone number.')
    print('5.Change a contact name.')
    print('6.Show contact list.')
    print('7.Press 0 to exit.')
    choose=int(input('Please enter a number : '))
    while choose<0 or choose>6:
        choose=int(input('Please enter a number within the range : '))
    if choose==0:
        break
    if choose==1:
        add(telbook)

    if choose==2:
        delete(telbook)
    
    if choose==3:
        search(telbook)
    
    if choose==4:
        change_number(telbook)

    if choose==5:
        change_name(telbook)

    if choose==6:
        show_all_contacts(telbook)

    
