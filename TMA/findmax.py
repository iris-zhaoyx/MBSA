import pandas as pd
import json
import os
import csv
import cv2
file_path="./1-2500.csv"
dicts = []
#重写文件
with open(file_path, encoding='utf-8') as f:
    csv_readers = csv.reader(f)
    for row in csv_readers:
        name=row[0]
        print("name",name)
        data1=row[1]
        print("data1",data1)
        max=data1
        mid=0
        data2=row[2]
        print("data2",data2)
        if data2>max:
            max=data2
            mid=1
        data3=row[3]
        print("data3",data3)
        if data3>max:
            max=data3
            mid=2
        data4=row[4]
        print("data4",data4)
        if data4>max:
            max=data4
            mid=3
        data5=row[5]
        print("data5",data5)
        if data5>max:
            max=data5
            mid=4
        data6=row[6]
        print("data6",data6)
        if data6 > max:
            max=data6
            mid=5
        data7=row[7]
        print("data7",data7)
        if data7>max:
            max=data7
            mid=6
        data8=row[8]
        print("data8",data8)
        if data8>max:
            max=data8
            mid=7
        data9=row[9]
        print("data9",data9)
        data10=row[10]
        print("data10",data10)
        data11=row[11]
        print("data11",data11)
        print("max,mid",max,mid)

        dict = [name,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,max,mid]
        dicts.append(dict)

with open('final.csv',"w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dicts)

