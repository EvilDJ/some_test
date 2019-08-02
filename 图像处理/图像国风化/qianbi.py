import cv2
import numpy as np
import math
from scipy import signal
#实现图像铅笔素描效果
img = cv2.imread('./3.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

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

img_sobel_x , img_sobel_y = sobel(im, 3)
# edge = img_sobel_x + img_sobel_y
edge = np.sqrt(np.power(img_sobel_x,2)+np.power(img_sobel_y,2))
# edge = (img_sobel_x + img_sobel_y)/2.0
edge = edge/np.max(edge)
edge*= 255
edge = edge.astype(np.uint8)
edge = 255 - edge
# cv2.imshow('pencil_edge',pencil_edge)
cv2.imshow('_img',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()