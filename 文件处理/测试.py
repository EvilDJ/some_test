import os
from PIL import Image
from glob import glob
import numpy as np
import random
# path = "F:\网络数据集\lfw\lfw"
# tra_01 = r"F:\网络数据集\lfw\调试代码"#存放匹配对象
# '''
# print(len(path))
path = r'F:/网络数据集/cacd数据集/CACD2000'
# "/".join(imageA.split("/")[-2:]), "/".join(imageB.split("/")[-2:])
#
num = 0
for dir_a, dir_n, file_n in os.walk(path):
    if file_n != []:
        # print(file_n)
        print(file_n[0])
        print(file_n[1])
        num += 1
        if num == 2:
            break
    
    
    # if file_n != []:
    #     print(file_n)
        #for i,val in enumerate(file_n):
         #   print(i,len(file_n))
         #   print(val)
#
#
# '''    # 文件夹下文件夹的路径，文件夹的名字，文件夹内的文件名字
# images = []
# folderList = glob(tra_01 + '\\*')
# print(tra_01)
# print(folderList)
# for folder_i, folder in enumerate(folderList):
#     imgPathList = glob(folder + '\\*' + 'jpg')
#     images.append(imgPathList)
# print(images)
# print(len(images))
#
# for i in range(images):
#     print("+++++++++++")
#     imageA = np.random.choice(images[i])
#     imageB = np.random.choice(images[i])
#     print("/".join(imageA.split("/")[-2:]), "/".join(imageB.split("/")[-2:]))
#     while (imageA == imageB):
#         imageB = np.random.choice(images[i])
# print("/".join(imageA.split("/")[-2:]), "/".join(imageB.split("/")[-2:]))