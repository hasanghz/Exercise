import os
currentDir=os.getcwd()+ '\Package'
os.chdir(currentDir)
from Package import Customer
from Package import Product


C1=Customer('Hasan','Ghaznavi','09378928796')
P1=Product('Mobile','12000000','20')