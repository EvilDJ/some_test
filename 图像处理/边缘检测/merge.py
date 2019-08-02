import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread('./2.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('img_gray',im)

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

#局部阈值
def local_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 25, 10)
    # cv2.namedWindow("binary1", cv2.WINDOW_NORMAL)
    # cv2.imshow("local", binary)
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

img_sobel_x , img_sobel_y = sobel(im, 7)
edge = img_sobel_x + img_sobel_y
edge = edge/np.max(edge)
edge*= 255
edge = edge.astype(np.uint8)
cv2.imshow('sobel',edge)

local_im = local_threshold(img)
# cv2.imshow("local", local_im)
custom_im = custom_threshold(img)
# cv2.imshow("custom", custom_im)
substract_im = custom_im - local_im
cv2.imshow('substract',substract_im)

new_im = cv2.merge([edge,im,substract_im])

cv2.imshow('new_img',new_im)
# cv2.imwrite('edge_.jpg',new_im)
cv2.waitKey(0)
cv2.destroyAllWindows()