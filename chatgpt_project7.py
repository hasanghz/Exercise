def prescriptions(filename):
    dic_Atorvastatin={}
    dic_Losartan={}
    dic_Metformin={}
    drugs={}
    lis=[]
    with open(filename,'r', encoding='utf-8') as file:
        for line in file:
            if not line:
                continue
            line=line.strip()
            parts=line.split(',')
            for i in range(len(parts)):
                try:
                    parts[i]=int(parts[i])
                except:
                    continue
            x=parts[0]
            dic={'Quantity':parts[1], 'Price':parts[2],'Date':parts[3]}
            drugs[parts[0]]=dic
    print(drugs['Atorvastatin']['Quantity'])
        



prescriptions('d:\\python\\exercise\\exercise\\project7.txt')

