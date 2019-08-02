import cv2
import numpy as np
from scipy import signal

img = cv2.imread('./4.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def g_conv(im,size,sigma):
    h,w = size
    xr,xc = np.mgrid[0:1,0:w]
    xc -= (w-1)/2
    xk = np.exp(-np.power(xc ,2.0))
    i_xk = signal.convolve2d(im,xk,'same','symm')
    yr,yc = np.mgrid[0:h,0:1]
    yr -= (h-1)/2
    yk = np.exp(-np.power(yr,2.0))
    i_xk_yk = signal.convolve2d(i_xk,yk,'same','symm')
    i_xk_yk *= 1.0/(2*np.pi*pow(sigma,2.0))
    return i_xk_yk
def dog(im,size,sigma,k=1.1):
    is_ = g_conv(im,size,sigma)
    isk = g_conv(im,size,k*sigma)
    dog = isk - is_
    dog /= (pow(sigma,2.0)*(k-1))
    return dog
sigma = 2
k = 1.1
size = (13.0,13.0)
img_dog = dog(im,size,sigma,k)
edge = np.copy(img_dog)
edge[edge>0]=255
edge[edge<=0]=0
edge = edge.astype(np.uint8)
cv2.imshow('edge',edge)
#抽象化
asbstraction = -np.copy(img_dog)
asbstraction = asbstraction.astype(np.float32)
asbstraction[asbstraction>=0]=1.0
asbstraction[asbstraction<0]=1.0+np.tanh(asbstraction[asbstraction<0])
asbstraction = asbstraction.astype(np.uint8)
cv2.imshow('asbstraction',asbstraction)
cv2.waitKey(0)
cv2.destroyAllWindows()
