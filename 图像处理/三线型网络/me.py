import cv2
import numpy as np
import math

def re(img):
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return cv2.resize(img,(225,225))

def d(img ,r):
    i,j = img.shape
    sum = 0
    for i1 in range(i):
        for j1 in range(j):
            sum += np.square(img[i1][j1] - r)
    return np.abs(sum / (i*j))

img_l = cv2.imread('./0.jpg')
img_l = re(img_l)
img_ = cv2.imread('./1.jpg')
img_ = re(img_)
img_r = cv2.imread('./3.jpg')
img_r = re(img_r)

img_l_ = img_l - img_
img_r_ = img_r - img_

al = np.mean(img_l_)
ar = np.mean(img_r_)

dl = d(img_l_,al)
dr = d(img_r_,ar)
print(dl,dr)
cv2.imshow('0',img_r_)
cv2.imshow('1',img_l_)
cv2.waitKey(0)
cv2.destroyAllWindows()