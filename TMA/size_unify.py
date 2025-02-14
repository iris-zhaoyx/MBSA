from PIL import Image
import json
import os
import csv
import cv2

def sort_min(temp1,temp2):
    if float(temp1)>float(temp2):
        return float(temp2)
    else:
        return float(temp1)

def sort_max(temp1,temp2):
    if float(temp1)>float(temp2):
        return float(temp1)
    else:
        return float(temp2)

def size_unify():
    srcPath ='./data/csv/'
    dstPath ='./data/size_unify/'
    #x_min=1280.0
    #y_min=720.0
    #x_max=0.0
    #y_max=0.0
    for root, dirs, files in os.walk(srcPath, topdown=False):
        for file in files:
            if ".csv" in file:
                jsonPath = root+file
                print("jsonPath:",jsonPath)
                name=file
                print("name:",name)
            x_min=1280.0
            y_min=720.0
            x_max=0.0
            y_max=0.0

            with open(jsonPath) as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    left = float(row[1])   # X-coordinate in the upper left corner
                    top = float(row[2])     # Y-coordinate in the upper left corner
                    right = float(row[1])+float(row[3])  # bottom right corner
                    bottom = float(row[2])+float(row[4]) # bottom right corner
                    print("x_min:",x_min)
                    print("left:",left)
                    x_min=sort_min(left,x_min)
                    y_min=sort_min(top,y_min)
                    x_max=sort_max(right,x_max)
                    y_max=sort_max(bottom,y_max)
                    print("x_max,y_max:",x_max,y_max)
                    
                       
                if x_min<0:
                    x_min=0
                if y_min<0:
                    y_min=0
                if x_max>1280:
                    x_max=1280
                if y_max>720:
                    y_max=720
            
            dicts = []
                
            #重写文件
            with open(jsonPath, encoding='utf-8') as f:
                csv_readers = csv.reader(f)
                for row in csv_readers:
                    img_name=row[0]
                    dict = [img_name,x_min,y_min,x_max,y_max]
                    dicts.append(dict)
            with open(name,"w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(dicts)            


if __name__ == "__main__":
    size_unify()
