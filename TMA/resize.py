import cv2
import numpy as np
import os

def letterboxs(im, new_shape=(m, n), color=(114, 114, 114), imgPath, dstPath):
    shape = im.shape[:2]         # 计算当前帧的宽高,shape[1]--宽，shape[0]--高

    # 判断传入的new_shape是否是一个整数
    if isinstance(new_shape, int):
        new_shape = (m, n)

    padding_width=0
    padding_heigh=0
    new_heigh,new_width=shape[0],shape[1]
    r=shape[0]/shape[1]
    if r>1:                  # 判断传入的图片shape高宽比是否大于1
        if shape[0]>n:
            new_heigh=n
            r1=n / shape[0]                    # 高直接缩放到640
            new_width=int(shape[1]*r1)           #按照高缩放比例缩小的宽，一定小于640，需要进行取整、填充
            padding_width=m-new_width         #宽度上一行需要填充的像素数量
        else:
            padding_heigh=n-shape[0]          #高度上一行需要填充的像素数量
            padding_width=m-shape[1]

    else:                 
        if shape[1]>m:   
            new_width=m                      
            r2=m / shape[1]                     # 宽直接缩放到640
            new_heigh=int(shape[0]*r2)           #按照高缩放比例缩小的宽，一定小于640，需要进行取整、填充
            padding_heigh=n-new_heigh
        else:
            padding_heigh=n-shape[0]          #高度上一行需要填充的像素数量
            padding_width=m-shape[1]
    
    new_unpad=(new_width,new_heigh)
    #print("new_unpad",new_unpad)
    im=cv2.resize(im,new_unpad)

    top,bottom = int(padding_heigh/2),int(padding_heigh-padding_heigh/2)                        # 上下两侧需要padding的大小
    left,right = int(padding_width/2),int(padding_width-padding_width/2)                 # 左右两侧需要padding的大小
    im = cv2.copyMakeBorder(im, top, bottom, left,right, cv2.BORDER_CONSTANT, value=color)              # 填充指定大小的固定像索值
    #print("top,bottom,left,right",top,bottom,left,right)
    im=cv2.resize(im,(m,n))
    impath=imgPath.split('/')[2]+'/'+imgPath.split('/')[3]
    print("impath",impath)
    save_dir=dstPath+impath
    cv2.imwrite(save_dir,im)

if __name__ == "__main__":
    filePath="./data/crop_images/"
    dstPath ='./data/resize_img/'
    for root, dirs, files in os.walk(filePath, topdown=False):
        for file in files:
            imgPath = root+'/'+file
            img=cv2.imread(imgPath)
            letterboxs(img, 640, 640), (114, 114, 114),imgPath,dstPath)



    
