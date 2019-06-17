#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET 

file = input("enter xml file: ")
xmlobject = ET.parse(file)
parent = xmlobject.getroot()
print("Attributes : \n")
for node in xmlobject.iter():
    print(node.attrib)
print("\n first 5 nodes: \n")
for i in range(5):
    print("node ",i," :\n")
    for j in range(61):
        print(parent[i][j][0].text)
    print("\n")


# In[2]:


import json
count = 0
list1 = []
last5list = []
file = input("enter json file: ")
with open(file) as f:
    data = json.loads(f.read())

for item in data:
    for key,val in item.items():
        type(val)
list1 = val.keys()
list1 = list(list1)
print("Below are all keys in JSON file:\n")
for item in list1:
    print(item)
print("\n")
print("Last 5 calEvent Objects are:\n")
last5calobj = data[len(data)-5:len(data)]
for item in last5calobj:
    count = count+1
    print("Obj ",count,":\n")
    print(item)
    print("\n")




    
    

        
        


# In[ ]:




