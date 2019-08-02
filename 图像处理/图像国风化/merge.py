import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread('./3.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

vec_el=np.pi/2.2
vec_az=np.pi/4.
depth=10.
a=np.asarray(im).astype('float')
grad=np.gradient(a)
grad_x,grad_y=grad
grad_x=grad_x*depth/100.
grad_y=grad_y*depth/100.
dx=np.cos(vec_el)*np.cos(vec_az)
dy=np.cos(vec_el)*np.sin(vec_az)
dz=np.sin(vec_el)
A=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1./A
a2=255*(dx*uni_x+dy*uni_y+dz*uni_z)
a2=a2.clip(0,255)
im1 = im.astype(np.uint8)

def pascalsmooth(n):
    pascalsmooth = np.zeros([1,n],np.float32)
    for i in range(n):
        pascalsmooth[0][i] = math.factorial(n - 1)/(math.factorial(i)*math.factorial(n-1-i))
    return pascalsmooth
def pascalDiff(n):
    pascaldiff = np.zeros([1, n],np.float32)
    pascal_smooth = pascalsmooth(n-1)
    for i in range(n):
        if i == 0:
            pascaldiff[0][i] = pascal_smooth[0][i]
        elif i == n-1:
            pascaldiff[0][i] = -pascal_smooth[0][i-1]
        else:pascaldiff[0][i] = pascal_smooth[0][i] - pascal_smooth[0][i-1]
    return pascaldiff
def getsobel(n):
    pascal_smooth_kernel = pascalsmooth(n)
    pascal_diff_kernel = pascalDiff(n)
    sobelkernel_x = signal.convolve2d(pascal_smooth_kernel.transpose(),pascal_diff_kernel,mode='full')
    sobelkernel_y = signal.convolve2d(pascal_smooth_kernel,pascal_diff_kernel.transpose(),mode='full')
    return sobelkernel_x,sobelkernel_y
def sobel(img,n):
    x,y = img.shape
    pascal_smooth = pascalsmooth(n)
    pascal_diff = pascalDiff(n)
    image_x = signal.convolve2d(img,pascal_smooth.transpose(),mode='same')
    image_x = signal.convolve2d(image_x,pascal_diff,mode='same')
    image_y = signal.convolve2d(im,pascal_smooth,mode='same')
    image_y = signal.convolve2d(image_y,pascal_diff.transpose(),mode='same')
    return image_x,image_y

img_sobel_x , img_sobel_y = sobel(im, 2)
# edge = img_sobel_x + img_sobel_y
edge = np.sqrt(np.power(img_sobel_x,2)+np.power(img_sobel_y,2))
# edge = (img_sobel_x + img_sobel_y)/2.0
edge = edge/np.max(edge)
edge*= 255
edge = edge.astype(np.uint8)
edge = 255 - edge

im2 = 0.5*im1 + 0.5*edge

asb = im2.astype(np.float32)
asb[asb>=255] = 100
asb[asb<100] = 125 *(1-np.tanh(asb[asb<100]))
asb = asb.astype(np.uint8)

cv2.imshow('1',asb)
cv2.waitKey(0)
cv2.destroyAllWindows()