# import pandas as pd
# data = pd.read_xml('sample2.xml')
# print(type(data))

dict = {
    'name' : 'raghav',
    'location' : 'Canada'
}

print(dict)
print(type(dict.keys()))
print(type(dict.values()))

for k in dict.keys():
    print( f"value of key {k} is {dict[k]} ")

 
for k,v in dict.items():
    a,b = k,v
    print( f"value of key {k} is {v} ")


