class square:
    def __init__(self,y):
        __x=0
    def __str__(self):
        s=(str(self.__x))
        return s

p=square(8)

p.x=11
print(p)
print(str(p))
