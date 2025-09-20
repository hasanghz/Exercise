class circle:
    pi=3.14
    r=0
    def area(self):
        print('Masahat is : ',self.pi*self.r**2)
    def perime(self):
        print('Mohit is : ',self.pi*self.r*2)

t=circle()
t.r=int(input('Please enter the R : '))
t.area()
t.perime()