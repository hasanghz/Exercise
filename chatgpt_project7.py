def prescriptions(filename):
    dic={}
    lis=[]
    with open(filename,'r', encoding='utf-8') as file:
        for line in file:
            if not line:
                continue
            line=line.strip()
            parts=line.split(',')
            for i in range(len(parts)):
                print(i)
                try:
                    parts[i]=int(parts[i])

                except:
                    continue
        print(parts)



prescriptions('d:\\python\\exercise\\exercise\\project7.txt')

