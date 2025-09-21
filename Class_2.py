class employee:
    def __init__(self,code,name,family,salary):
        self.code=code
        self.name=name
        self.family=family
        self.salary=salary
            
    def caltax(self):
        if self.salary<=1500:
            print('Tax is 0')
        else:
            print('Tax is : ',(self.salary-1500)*0.1)
        return ((self.salary-1500)*0.1)
    
    def calinsurance(self):
        print('The insurance fee is : ',self.salary/10)
        return(self.salary*0.1)
    
    def pay(self):
        return (self.salary-self.salary.calinsurance-self.salary.caltax)
    

p1=employee(1,'Hasan','Ghaznavi',2000)


p2=employee(2,'Shiva','Alipour',1000)
print(p1.calinsurance())