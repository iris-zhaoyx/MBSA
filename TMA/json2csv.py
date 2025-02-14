import json
import os
import csv
import cv2
 
def decode_json(img_w, img_h):
    
    for root, dirs, files in os.walk("./data/json", topdown=False):
        dicts = []
        name=(root.split('/'))[-1]
        for file in files:
            print("file:",file)
            if ".json" in file:
                jsonPath = root+'/'+file
                
                #读取标注文件
                with open(jsonPath, encoding='utf-8') as f:
                    line = f.readline()
                    viaJson = json.loads(line)
                    for i in range(len(viaJson)-1):
                        data=viaJson[i]['key'].split(' ')
                        if int(data[0])==1:
                            x1 = float(data[1])
                            y1 = float(data[2])
                            x2 = float(data[3])
                            y2 = float(data[4])

                            width=x2*img_w
                            height=y2*img_h
                            x_min=(x1-0.5*x2)*img_w
                            y_min=(y1-0.5*y2)*img_h
                            
                            frameId=(((jsonPath.split('/'))[-1]).split('.'))[0]
                            print("frameId:",frameId)
                            dict = [frameId,x_min,y_min,width,height]
            dicts.append(dict)
        with open('./data/csv/'+name+'.csv',"w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dicts)          

 
if __name__ == "__main__":
    img_w = 1280
    img_h = 720
    decode_json(img_w, img_h)
