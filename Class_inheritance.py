class person:
    def __init__(self,code,Fname,Lname):
        self.code=code
        self.Fname=Fname
        self.Lname=Lname
    
    def __str__(self):
        s=f'Code is {self.code}\n First name is {self.Fname} \n Last name is {self.Lname}'
        print(s)
    

class student(person):
    def __init__(self,code,Fname,Lname,sum):
        super().__init__(code,Fname,Lname)
        self.sum=sum
        

    def __del__(self):
        print('Object is deleted')
    
    def ispass(self):
        if self.sum> 12:
            s=(f'Student {self.Lname} is passed')
            return s
        else:
            s=(f'Student {self.Lname} is failed')
            return s

    def __str__(self):
        t=f'The student{self.Fname} {self.Lname} code {self.code} , sum is {self.sum} and he or she is {self.ispass()}'
        print(t)

class employee(person):
    def __init__(self,code,Fname,Lname,salary):
        super().__init__(code,Fname,Lname)
        self.salary=salary
    
    def __del__(self):
        print('The object is deleted')

    def tax(self):
        if self.salary>1500:
            t=self.salary/10
        else:
            t=0
        return t

    def insurance(self):
        i=self.salary/20
        return i

    def pay(self):
        p=(self.salary-self.tax-self.isinstance)
        return p
    
    def __str__(self):
        s=f'Employee {self.Fname,self.Lname} code {self.code} pay is {self.pay()} \n The tax is {self.tax} \n The insurance is {self.insurance}'
    
count=0
kount=0
while 1:
    
    print('Please enter the functions number : ')
    print('1 : Adding an employee.')
    print('2 : Adding a student. ')
    print('0 : Exit the program')
    func=int(input())
    if func==0:
        break

    if func == 1:
        
        E=[]
        emp=input('Please enter the code, first name, last name and salary . ')
        att=emp.split()
        E[count]=employee(att[0],att[1],att[2],att[3])
        print(str(E[count]))
        count+=1

    elif func ==2:
        S=[]
        std=input('Please enter the code, first name, last name and sum. ')
        ls=std.split()
        S[kount]=student(ls[0],ls[1],ls[2],ls[3])
        print(str(S[count]))
        kount+=1

           



        

