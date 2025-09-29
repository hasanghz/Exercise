class square:
    __x=0
    def __str__(self):
        s=f'{self.__x}'
        return s

p=square()

p.x=11
print(p)
print(str(p))
