from collections import OrderedDict
sales={'Aspirin':1200,'VitaminC':980,'Ibuprofen':1100,'Omeprazole':1250,'Cetirizine':1000}
total_sale=0
mean=0
over_1100=[]
share={}
for i in sales:
    total_sale+=sales[i]
    
    if sales[i]>1100:
        over_1100.append(i)
for i in sales:
    share[i]=round((sales[i]/total_sale*100),2)
mean=total_sale/len(sales)
min_sale=min(sales,key=sales.get)
max_sale=max(sales,key=sales.get)

print(f'The minimum sale is {min_sale}:{sales[min_sale]} \nThe maximum sale is {max_sale} : {sales[max_sale]}\nThe mean is {mean}\nTotal sale is :{total_sale}\nThe over 1100 sale is :{over_1100}\nThe share of each drug is :{share}')