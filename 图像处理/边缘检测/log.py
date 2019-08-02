import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread('./11.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def kernel(sigma,size):
    h,w = size
    r,c = np.mgrid[0:h:1,0:w:1]
    r -= (h-1)/2
    c -= (w-1)/2
    sigma = pow(sigma, 2)
    norm2 = np.power(r,2) + np.power(c,2)
    ker = (norm2/sigma -2)*np.exp(-norm2/(2*sigma))
    return ker
def log(image,sigma,size,_b):
    ker = kernel(sigma,size)
    img_conv = signal.convolve2d(image,ker,mode='same',boundary=_b)
    return img_conv
img_log = log(im,2,(100.0,37.0),'symm')
img_log[img_log>0]=255
img_log[img_log<=0]=0
img_log = img_log.astype(np.uint8)
cv2.imshow('log',img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()