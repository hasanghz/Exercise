def for_file(ls,number):
    main_file=open('D:\\Python\\Exercise\\Exercise\\text5.txt','wt')
    for i in range(number):
        t=open(ls[i])
        for line in t:
            main_file.write(line)
    main_file.close()

lis=[]
number=int(input('Please enter the number of files : '))
for i in range(number):
    x=input('Please enter the address of file : ')
    lis.append(x)

for_file(lis,number)



