file1=open('D:\\Python\\Exercise\\Exercise\\file1.txt','wt')
s1='Im the file 1 and im ready to exchange my data with file 2'
file1.write(s1)
file2=open('D:\\Python\\Exercise\\Exercise\\file2.txt','wt')
s2='Hello im file2 and im ready to tranfer my data to file 1'
file2.write(s2)
file2.close()

file2=open('D:\\Python\\Exercise\\Exercise\\file2.tex','tw')
while 1:
    s3=file1.readline()
    if len(s1)==0:
        break
    file2.write(s2)

t=file2.read()
print(t)
file2.close()
file1.close()
