from collections import OrderedDict
dic={}
while 1:
    x=input('Please enter the name of medicine : ')
    y=input('Please enter the batch numbers : ')
    if x=='0' or y=='0':
        break
    lis=y.split()
    dic[x]=lis
    if x=='0' or y=='0':
        break

for i in dic:
    print(i,dic[i])

def get_latest_batch(x):
    y=input('please enter the name of the medicine to receive the latest batch number : ')
    value=x.setdefault(y,'Drug was not found')
    t=len(value)-1
    print('The latest batch is : ',value[t])

get_latest_batch(dic)