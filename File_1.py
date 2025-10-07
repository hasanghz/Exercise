myfile=open('D:\\Python\\Exercise\\Exercise\\First_file.txt','wt')

while 1:
    s=input('Please enter a sentence : ')
    if len(s)==0:
        break
    s+='\n'
    myfile.write(s)
myfile.close()
