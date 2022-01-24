# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import random

#img = cv2.imread('4.jfif')
def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    shuchu = cv2.warpAffine(image, M, (nW, nH))
    return shuchu
    #while (1):
        #cv2.imshow('shuchu', shuchu)
        #if cv2.waitKey(1) & 0xFF == 27:
            #break

#rotate_bound(img, 45)
index=0
img_path='./datasets/train/cat/'
saveimg_path='./datasets/train/cat_flip1/'
label_path='./datasets/train/dog/'
savelabel_path='./datasets/train/dog_flip1/'
if not os.path.exists("./datasets/train/cat_flip1/"):
    os.makedirs("./datasets/train/cat_flip1/")
if not os.path.exists("./datasets/train/dog_flip1/"):
    os.makedirs("./datasets/train/dog_flip1/")
for filename in os.listdir(label_path):  # listdir的参数是文件夹的路径,listdir用于返回指定文件夹文件名字列表
    a=random.randint(-180, 180)
    print(a)
    index = index + 1
    imgname = filename[:-4]
    print(imgname)
    #img = cv2.imread(img_path + filename)  # 加'/',否则读不进图像。。。
    label = cv2.imread(label_path+filename)
    #img =rotate_bound(img,a)
    label=rotate_bound(label,a)
    #img = img[0:160,0:160,:]
    #label = label[0:160, 0:160, :]
    #cv2.imwrite(saveimg_path+'cat.'+str(39955+index)+'.jpg',img)
    cv2.imwrite(savelabel_path +'dog.'+ str(39979 + index) + '.jpg', label)