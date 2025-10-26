from datetime import datetime
time=datetime.today().strftime('%Y-%m-%d')
myfile=open('d:\\python\\exercise\\exercise\\Drug.txt','+r')
time_split=time.split('-')
time_split=list(map(int, time_split))

for line in myfile.readlines():
    lis=line.split(',')
    lis[1]=lis[1].split
    print(lis[1])
    print(time_split)
