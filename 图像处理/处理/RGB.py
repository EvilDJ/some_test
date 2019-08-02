import cv2 as cv
import numpy as np

img = cv.imread('F:\pycharm_代码\图像处理/2.jpg')
print(img)
b,g,r = cv.split(img)
print(img.shape)
a=np.ones((338,600,3))
c=cv.subtract(a,img)
print(b)
#print(g)
#print(r)

#cv.imshow("blue",b)
#cv.imshow("red",r)
#cv.imshow("green",g)
'''
def get_red(img):
    redImg = img[:,:,2]
    return redImg

def get_green(img):
    greenImg = img[:,:,1]
    return greenImg

def get_blue(img):
    blueImg = img[:,:,0]
    return blueImg

b = get_blue(img)
g = get_green(img)
r = get_red(img)
cv.imshow("blue1",b)
cv.imshow("red1",r)
cv.imshow("green1",g)
'''

cv.waitKey (0)
cv.destroyAllWindows()