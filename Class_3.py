class square:
    def __inint__(self,__x):
        self.__x=__x
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
        perime=f'The perime is : {self.__perime}'
        area=f'The area is :{self.__area}'
        return perime , area

x=int(input('Please enter the amount of side :'))
x=square()    
print(str(x))



