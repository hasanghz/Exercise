from collections import OrderedDict
def prescriptions(filename):
    total_sale={}
    drugs={}
    lis=[]
    most_sale={}
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
            
            dic={'Quantity':parts[1], 'Price':parts[2],'Date':parts[3]}
            if parts[0] in drugs:
                
                total_sale[parts[0]]+=parts[2]*parts[1]
            else:
                total_sale[parts[0]]=parts[2]*parts[1]

            
            if parts[0] in drugs:

                most_sale[parts[0]]+=parts[1]
            else:
                most_sale[parts[0]]=parts[1]
            drugs[parts[0]]=dic

    print(drugs,'\n',total_sale,'\n',f'The maximum sale is : {max(most_sale)} and {(most_sale[max(most_sale)])}')
        



prescriptions('d:\\python\\exercise\\exercise\\project7.txt')

