import os
import json

image_files = []

for file in os.listdir():
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        image_files.append(file)

with open('names.txt','r',encoding='utf-8') as f:
    names = f.read().split(' ')

image_map = list(zip(names,image_files))
print(image_map)

result = list(map(lambda f:{
    "name":f[0],
    "isNew":False,
    "isOriginal":False,
    "hasOtherForm":False,
    "hasOtherConcept":False,
    'type':None,
    'picUrl':f[1],
    }, image_map))

print(result[0])

with open('rocodex.json','w') as f:
    f.write(json.dumps(result))
