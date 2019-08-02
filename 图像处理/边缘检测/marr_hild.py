import cv2
import numpy as np
from 边缘检测 import dog as dg

img = cv2.imread('./11.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def zero_cross_default(dog):
    zero_cross = np.zeros(dog.shape,np.unit8)
    r,c = dog.shape
    for i in range(1,r-1):
        for j in range(1,c-1):
            if dog[r][c-1]*dog[r][r+1]<0:
                zero_cross[r][r] = 255
                continue
            if dog[r-1][c]*dog[r+1][c] < 0:
                zero_cross[r][r] = 255
                continue
            if dog[r-1][c-1]*dog[r+1][c+1]<0:
                zero_cross[r][r] = 255
                continue
            if dog[r-1][c+1]*dog[r+1][c-1]<0:
                zero_cross[r][c] = 255
                continue
    return zero_cross
def zero_cross_mean(dog):
    zero_cross = np.zeros(dog.shape,np.uint8)
    formean = np.zeros(4,np.float32)
    r,c = dog.shape
    for i in range(1,r-1):
        for j in range(1,c-1):
            lefttop = np.mean(dog[r-1:r+1,c-1:c+1])
            formean[0] = lefttop
            righttop = np.mean(dog[r-1:r+1,c:c+2])
            formean[1] = righttop
            leftbottom = np.mean(dog[r:r+2,c-1:c+1])
            formean[2] = leftbottom
            rightbottom = np.mean(dog[r:r+2,c:c+2])
            formean[3] = rightbottom
            if(np.min(formean)*np.max(formean)<0):
                zero_cross[r][c] = 255

    return zero_cross
def marr(im,size,sigma,k=1.1,cross_type = 'ZERO_CROSS_DEFAULT'):
    d = dg.dog(im,size,sigma,k)
    if cross_type == 'ZERO_CROSS_DEFAULT':
        zero_cross = zero_cross_default(d)
    elif cross_type == 'ZERO_CROSS_MEAN':
        zero_cross = zero_cross_mean(d)

    return zero_cross

result = marr(im,(37.0,37.0),6,1.1,'ZERO_CROSS_MEAN')
cv2.imshow('marr',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

