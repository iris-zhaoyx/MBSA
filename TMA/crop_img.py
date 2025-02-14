from PIL import Image
import json
import os
import csv
import cv2

def crop_img():
    filePath= img_file_path
    srcPath = csv_file_path
    dstPath = dst_path
    for root, dirs, files in os.walk(srcPath, topdown=False):
        for file in files:
            if ".csv" in file:
                jsonPath = root+file
                print("jsonPath:",jsonPath)

            with open(jsonPath) as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    img_name=row[0]
                    img_path=filePath+(file.split('.'))[0]+'/'+img_name+'.jpg'
                    print("img_path:",img_path)

                    image = Image.open(img_path)
                    left = float(row[1])   # 左上角x坐标
                    top = float(row[2])     # 左上角y坐标
                    right = float(row[3])  # 右下角x坐标
                    bottom = float(row[4]) # 右下角y坐标
                    box = (left, top, right, bottom)
                    print("box",box)
                       
                    # 裁剪图像
                    cropped_image = image.crop(box)

                    # 保存裁剪后的图像
                    imgPath=dstPath+(file.split('.'))[0]+'/'+img_name+'_0.jpg'
                    print(imgPath)
                    cropped_image.save(imgPath)


if __name__ == "__main__":
    crop_img()





 

 

 
