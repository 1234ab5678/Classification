import cv2
import os
import tqdm

def flip(img, dir):
    """

    :param img:
    :param dir: 1-horizontal, 0-vertical, -1:horizontal&vertical
    :return:
    """
    return cv2.flip(img, dir)

index=0
img_path='./datasets/train/cat/'
save_path='./datasets/train/cat_flip1/'
if not os.path.exists("./datasets/train/cat_flip1/"):
    os.makedirs("./datasets/train/cat_flip1/")
for filename in os.listdir(img_path):  # listdir的参数是文件夹的路径,listdir用于返回指定文件夹文件名字列表
    index = index + 1
    imgname = filename[:-4]
    print(imgname)
    img = cv2.imread(img_path + filename)  # 加'/',否则读不进图像。。。
    img =cv2.flip(img,-1)
    cv2.imwrite(save_path+'cat.'+str(29966+index)+'.jpg',img)