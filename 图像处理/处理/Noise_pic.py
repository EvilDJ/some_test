# -*- coding: utf-8 -*-
from scipy import *
import numpy as np
import cv2
from PIL import Image as image

#定义添加椒盐噪声的函数
def SaltAndPepper(src,percetage):
    SP_NoiseImg=src
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            SP_NoiseImg[randX,randY]=0
        else:
            SP_NoiseImg[randX,randY]=255
    return SP_NoiseImg

#定义添加高斯噪声的函数
def addGaussianNoise(image,percetage):
    G_Noiseimg = image
    G_NoiseNum=int(percetage*image.shape[0]*image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(20,40)
        temp_y = np.random.randint(20,40)
        G_Noiseimg[temp_x][temp_y] = 255
    return G_Noiseimg

#二值化 全局阈值
def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("threshold value %s"%ret)
    return binary
    # cv2.namedWindow("binary0", cv2.WINDOW_NORMAL)
    # cv2.imshow("threshold", binary)

#局部阈值
def local_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 25, 10)
    # cv2.namedWindow("binary1", cv2.WINDOW_NORMAL)
    # cv2.imshow("local", binary)
    print(binary)
    return binary
#用户自己计算阈值
def custom_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    h, w =gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    # mean = m.sum()/(w*h) # 6.1
    mean = 7
    # print("mean:",mean)
    ret, binary =  cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
    # cv2.namedWindow("binary2", cv2.WINDOW_NORMAL)
    # cv2.imshow("custom", binary)
    return binary

#反色处理
def access_pixels(image):
    height, width = image.shape
    # print("width:%s,height:%s,channels:%s" % (width, height))

    for row in range(height):
        for list in range(width):
            pv = image[row, list]
            image[row, list] = 255 - pv
    cv2.imshow("AfterDeal", image)

im = cv2.imread('./3.jpg')
# print(im.shape,type(im))
# cv2.imshow('original pic',im)
# demo_im = threshold_demo(im)
local_im = local_threshold(im)
cv2.imshow("local", local_im)
custom_im = custom_threshold(im)
cv2.imshow("custom", custom_im)
substract_im = custom_im - local_im
cv2.imshow('substract',substract_im)
access_pixels(substract_im)


# gauss_noiseImage = addGaussianNoise(im, 0.1)  # 添加10%的高斯噪声
# cv2.imshow('gauss pic',gauss_noiseImage)
# cv2.imwrite("Gauss_pic_2.jpg ", gauss_noiseImage)
# print(gauss_noiseImage.shape,type(gauss_noiseImage))
# SaltAndPepper_noiseImage = SaltAndPepper(im, 0.04)  # 再添加10%的椒盐噪声
# cv2.imshow('salt pic',SaltAndPepper_noiseImage)
# cv2.imwrite("Salt_pic_2.jpg ", gauss_noiseImage)
# print(SaltAndPepper_noiseImage.shape,type(SaltAndPepper_noiseImage))
cv2.waitKey(0)
cv2.destroyAllWindows()

