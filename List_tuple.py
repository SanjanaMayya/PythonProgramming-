d = {'Name' : 'Ram' , 'Age' : '19' , 'Country' : 'India'}
print(d.items())        #Output: dict_items([('Name', 'Ram'), ('Age', '19'), ('Country', 'India')])
print(list(d.items()))      #Output:[('Name', 'Ram'), ('Age', '19'), ('Country', 'India')]
for k,v in d.items():
    print(k,v,sep=': ')      #Output: Name: Ram, Age: 19, Country: India
print(list(d.items())[1][0])  #Output: Age
print(list(d.items())[1][1])    #Output: 19
print(d.keys())   #Output: dict_keys(['Name','Age','Country'])
print(d.values())  #Output: dict_values(['Ram','19','India'])
print(list(d.keys()))   #Output: ['Name','Age','Country']
print(list(d.values()))  #Output: ['Ram','19','India']