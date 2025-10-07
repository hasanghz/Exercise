class Product:
    def __init__(self,name,price,discount):
        self.name=name
        self.price=int(price)
        self.discount=int(discount)
    
    def __str__(self):
        s=f'Product name is {self.name} \n Price is {self.price} \n {self.discount}'
        return s
    
    def pay(self):
        return self.price-self.discount()

    def __del__(self):
        print('object is deleted')

    def discount(self):
        return self.price*0.8

    def __repr__(self):
        return self.__str__()
    
pr=[]
tr=[] 
kount=int(input('Please enter the number of products :'))
for i in range (kount):
    p=input('Please enter the product information in order of name, price and discount :')
    lp=p.split()
    pr.append(Product(lp[0],lp[1],lp[2]))
    tr.append(lp)

for x in range(len(pr)):
    print(pr[x].name)
    print(pr)
    print(tr)
    print(tr[x][0])




