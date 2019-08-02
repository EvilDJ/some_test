import cv2
import numpy as np

def re(img):
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return cv2.resize(img,(225,225))

def d(l ,r):
    i,j = l.shape
    sum = 0
    for i1 in range(i):
        for j1 in range(j):
            sum += np.square(l[i1][j1] - r[i1][j1])
    return np.abs(sum / (i*j))

img_l = cv2.imread('./0.jpg')
img_l = re(img_l)
img_ = cv2.imread('./1.jpg')
img_ = re(img_)
img_r = cv2.imread('./3.jpg')
img_r = re(img_r)

l_ = d(img_l, img_)
r_ = d(img_, img_r)

print(l_, r_)