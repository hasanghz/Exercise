def file(file_path):
    for p in file_path:
        file1=open(p,'+r')
        x=input('Please enter a string')
        file1.write(x)
        lines=file1.read()
        print(lines)
        file1.close()
paths=['D:\\Python\\Exercise\\Exercise\\text3.txt','D:\\Python\\Exercise\\Exercise\\file1.txt','D:\\Python\\Exercise\\Exercise\\file2.txt']
file(paths)