import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread("./2.jpg")
hight, width, depth = img.shape

#图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))

#创建形状和尺寸的结构元素
kernel = np.ones((3, 3), np.uint8)

#扩张待修复区域
hi_mask = cv2.dilate(thresh, kernel, iterations=1)
specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

im = cv2.cvtColor(specular, cv2.COLOR_RGB2GRAY)
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
    #水平方向上的卷积核
    sobelkernel_x = signal.convolve2d(pascal_smooth_kernel.transpose(),pascal_diff_kernel,mode='full')
    #垂直方向上的卷积核
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

img_sobel_x , img_sobel_y = sobel(im, 8)
edge = np.sqrt(np.power(img_sobel_x,2)+np.power(img_sobel_y,2))
edge = edge/np.max(edge)
edge*= 255
edge = edge.astype(np.uint8)
edge = 255 - edge

def scharr(img):
    scharr_x = np.array([[3,0,-3],[10,0,-10],[3,0,-3]],np.float32)
    img_x = signal.convolve2d(img,scharr_x,mode='same',boundary='symm')
    scharr_y = np.array([[3,10,3],[0,0,0],[-3,-10,-3]],np.float32)
    img_y = signal.convolve2d(img,scharr_y,mode='same',boundary='symm')
    return img_x,img_y

conv_x, conv_y = scharr(im)
edge_x = np.abs(conv_x).copy()
edge_y = np.abs(conv_y).copy()
edge_x[edge_x>255] = 255
edge_y[edge_y>255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
edge_s = edge_y + edge_x
# edge = np.abs(edge_x -edge_y)
edge_s[edge_s>255] = 255
edge_s = edge_s.astype(np.uint8)

cv2.imshow("Scharr", edge_s)
cv2.imshow("Sobel", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()