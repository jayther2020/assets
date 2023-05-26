import os
import json

image_files = []

for file in os.listdir():
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        image_files.append(file)

result = list(map(lambda f:{
    "name":'测试花瓶',
    "isNew":False,
    'type':None,
    'picUrl':f,
    }, image_files))

with open('rocodex.json','w') as f:
    f.write(json.dumps(result))
