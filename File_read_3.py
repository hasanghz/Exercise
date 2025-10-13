def filter_file(old_file,new_file,n):
    oldfile=open(old_file,'rt')
    newfile=open(new_file,'wt')
    matn=oldfile.read(n)
    
    newfile.write(matn)
    
    newfile.close()
    oldfile.close()

filter_file('D:\\Python\\Exercise\\Exercise\\text3.txt','D:\\Python\\Exercise\\Exercise\\text4.txt',5)

