def replace(address):
    newfile=open('d:\\python\\exercise\\exercise\\text6.txt','wt')
    with open(address) as myfile:
        for line in myfile:
            newfile.write(line)
            newfile.seek(0)
    newfile.close()

x='d:\\python\\exercise\\exercise\\text5.txt'
replace(x)

