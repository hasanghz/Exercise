from collections import OrderedDict
def menu():
    while 1:
        choose=int(input('Please enter a number : '))
        print('1.Add a contact.')
        print('2.Delete a contact.')
        print('3.Search a contact.')
        print('4.Change a phone number.')
        print('5.Change a contact name.')
        print('6.Show contact list.')