myfile=open('D:\Python\exercise\exercise\First_file.txt','r')
while 1:
    
    s=myfile.readline()
    print(s)
    if len(s)==0:
        break

myfile.close()
