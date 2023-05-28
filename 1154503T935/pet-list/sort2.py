import os
import json

image_files = []

for file in sorted(os.listdir()):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        image_files.append(file)

with open('names.txt','r',encoding='utf-8') as f:
    names = f.read().split(' ')

image_map = list(zip(names,image_files))
print(image_map)

result = list(map(lambda f:{
    "id":f[0]+1,
    "name":f[1][0],
    'picUrl':f[1][1],
    'type':None,
    "isNewDetail":{"isNew":False,"derivedFrom":None,"derivedFromPicUrl":None},
    "isOriginalDetail":{"isOriginal":False,"originalAuthor":None},
    "hasOtherFormDetail":{"hasOtherForm":False,"otherFormInfo":[{"otherFormPic":None,"otherFormDesc":None}]},
    "hasOtherConceptDetail":{"hasOtherConcept":False,"otherConceptInfo":[{"otherConceptPic":None,"otherConceptDesc":None}]},
    "evolutionChain":[],
    "petView":[],
    "petExpressionView":[],
    "petMovesView":[],
    "petGallery":[],
    }, list(enumerate(image_map))))

print(result[0])

with open('rocodex-pet-detail.json','w') as f:
    f.write(json.dumps(result))
