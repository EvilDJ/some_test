import  cv2
import  numpy as np
'''
def blur_demo(image):#平均模糊
    dst = cv2.blur(image,(5,5))
    cv2.imshow('dst',dst)


def median_blur_demo(image):#中值模糊
    dst = cv2.medianBlur(image,5)

def custom_blur_demo(image):#自定义卷积核
    # kernol = np.ones((5,5),np.float32)/25
    kernol = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)#总和等于0或者总和等于1
    dst = cv2.filter2D(image,-1,kernol)
    cv2.imshow('custom_blur',dst)


src = cv2.imread('E:\临时文件夹\wx.jpg')
blur_demo(src)
custom_blur_demo(src)
cv2.imshow('src',src)
cv2.waitKey(0)
'''
image = cv2.imread("wx.jpg")
dst = cv2.blur(image,(5,5))
cv2.imshow('dst',dst)
cv2.waitKey(0)