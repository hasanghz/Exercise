class customer:
    def __init__(self,fname,lname,tel):
          self.fname=fname
          self.lname=lname
          self.tel=tel

    def __del__(self):
        print('object is deleted')

    def __str__(self):
         s=f'Customer name is {self.fname} {self.lname}\n'
         s+=f'Customer phone number is {self.tel}'
         return s
    def __repr__(self):
         return self.__str__()
count=int(input('Please enter the number of customers :'))
cs=[]

for i in range (count) :
     
    f1=input('Please enter the first,last name and phone number : ')
    ls=f1.split()
    cs.append(customer(ls[0],ls[1],ls[2]))
    
for x in range (len(cs)):
     
    print(cs[x].fname)


