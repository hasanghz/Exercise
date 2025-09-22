class employee:
    def __init__(self,code,name,family,salary):
        self.code=code
        self.name=name
        self.family=family
        self.salary=salary
            
    def caltax(self):
        if self.salary<=1500:
            return 0
        else:
            
            return ((self.salary-1500)*0.1)
    
    def calinsurance(self):
        
        return(self.salary*0.1)
    
    def pay(self):
        return (self.salary-self.calinsurance()-self.caltax())
        

    def __str__(self):
        return f'The employee\'s name is {self.name,self.family} \n The salary is : {self.pay()} \n The Insurance fee is {self.calinsurance()} \n The tax fee is : {self.caltax()}'


p1=employee(1,'Hasan','Ghaznavi',2000)
p2=employee(2,'Shiva','Alipour',1000)

print(str(p1),'\n',str(p2))
