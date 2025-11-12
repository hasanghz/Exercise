with open('d:/python/exercise/exercise/raw_data.txt') as myfile:
    dic={}
    for line in iter(myfile.readline,''):
         
         line=line.strip()
         word=line.split(',')
         try:
              num=float(word[1])
              if word[0] !='':
                   dic[word[0]]=word[1]
         except ValueError:
              continue
            
    print(dic.items())