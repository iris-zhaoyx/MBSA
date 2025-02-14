import argparse
import cv2
import numpy as np
import json
import copy
import random
import os
import glob
import time

def img_preprocess(img_path,output_path):
    for im_path in sorted(glob.glob(os.path.join(img_path, '*.png'))):
        im = cv2.imread(os.path.abspath(im_path),-1)
        im = ((im / im.max()) * 255)
        im = im.astype('uint8')
        if im is None:
            break
        str0 = os.path.basename(im_path)
        out_images_names=output_path+str0
        cv2.imwrite(out_images_names,im)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgpathin', type=str, default='/home/a309/iris/images', help='initial images path')
    parser.add_argument('--imgpathout', type=str, default='/home/a309/iris/images/', help='use weighted image selection for training')

    opt = parser.parse_args()

    t0 = time.time()

    img_preprocess(opt.imgpathin, opt.imgpathout)
    print('Done. (%.3fs)' % (time.time() - t0))



