from pycocotools.coco import COCO
import json
from json import encoder
dataDir='.'
dataType='train2014'
annfile='../annotations/instances_train2014.json'
coco = COCO(annfile)
info = coco.info()
img_ids = 11
anno_ids = coco.getAnnIds([15],[15],[0],True)
print(anno_ids)
annos = coco.loadAnns(anno_ids)
print(annos)
for each in coco.dataset['annotations']:
    print("Annotations")
    print(json.dumps(each,indent=4))
  #  for i in each:
  #      print(str(i) + ":" + str(each[i]))

 #   print("\n------------------------------------------")
