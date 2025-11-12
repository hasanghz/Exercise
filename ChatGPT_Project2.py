from datetime import datetime
time=datetime.today().strftime('%Y-%m-%d')
myfile=open('d:\\python\\exercise\\exercise\\Drug.txt','+r')
time_split=time.split('-')
time_split=list(map(int, time_split))

for line in myfile.readlines():
    lis=line.split(',')
   # lis[1]=lis[1].split()
    expire=lis[1].split('-')
    expire=list(map(int, expire))
    expire_day=(expire[0]*365)+(expire[1]*30)+(expire[2])
    time_day=(time_split[0]*365)+(time_split[1]*30)+(time_split[2])
    if expire_day-time_day <0 :
        print(f'{lis[0]} has expired')
    elif expire_day-time_day >0 and expire_day-time_day<90 :
        print(f'{lis[0]} will expire soon !')

    elif expire_day-time_day > 90:
        print(f'{lis[0]} expire date is valid')
    
   

