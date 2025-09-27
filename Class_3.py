class square:
    
    def __init__(self,x):
        self.__x=x
    def __area(self):
        area=self.__x**2
        return area
    def __perime(self):
        perime=self.__x*4
        return perime
    def set(self,x):
        self.__x=x
    def get(self):
        return self.__x
    def __str__(self):
        s=f'X is {x} \n'
        s+=f'The perime is : {self.__perime()} \n'
        s+=f'The area is :{self.__area()}'
        return s
x=int(input("Enter a number : "))
s=square(x)
print(str(s))

s.x=4
print(s)



