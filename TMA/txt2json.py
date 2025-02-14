import json
import os
import csv
import cv2

for root, dirs, files in os.walk("./runs/detect/exp/labels", topdown=False):
    for file in files:

        file_path=root+'/'+file
        with open(file_path, 'r') as f:
            name = file.split('.')
            content = f.read()
            lines = content .split('\n')

            json_data=[]
            for line in lines:
                data={}
                data['key']=line
                json_data.append(data)

            json_content=json.dumps(json_data)

        with open('./data/json/'+name[0]+'.json',"w") as jsonfile: 
            jsonfile.write(json_content)
