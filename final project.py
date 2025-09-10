###final project
import hashlib
from collections import OrderedDict
import csv
password = OrderedDict()

with open('D:/python/exercise/hash.csv') as f:
    x=csv.reader(f)
    
    for row in x:
        password[row[0]]=row[1]
    print(password)
    
    for i in range(1000,10000):
        i=str(i)
        hashed=hashlib.sha256(i.encode())
        hashed=hashed.hexdigest()
        for read in password.values():
                if hashed in read:
                     print(i)
    
