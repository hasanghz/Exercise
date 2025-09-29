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
        self.code=code
        self.Fname=Fname
        self.Lname=Lname
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
        self.code=code
        self.Fname=Fname
        self.Lname=Lname
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
    
    
           



        

