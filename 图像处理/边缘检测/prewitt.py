import cv2
import numpy as np
from scipy import signal

img = cv2.imread('./11.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def prewitt(img):
    #1: 垂直方向上的均值平滑
    y = np.array([[1],[1],[1]],np.float32)
    conv_x = signal.convolve2d(img,y,mode='same',boundary='symm')
    #2: 水平方向上的差分
    x = np.array([[1,0,-1]],np.float32)
    conv_x = signal.convolve2d(conv_x,x,mode='same',boundary='symm')
    #1:水平方向上的均值平滑
    flat_x = np.array([[1,1,1]],np.float32)
    conv_y = signal.convolve2d(im,flat_x,mode='same',boundary='symm')
    #2:垂直方向上的差分
    flat_y = np.array([[1],[0],[-1]],np.float32)
    conv_y = signal.convolve2d(conv_y,flat_y,mode='same',boundary='symm')
    return (conv_x,conv_y)
#反色处理
def access_pixels(image):
    height, width = image.shape
    # print("width:%s,height:%s,channels:%s" % (width, height))

    for row in range(height):
        for list in range(width):
            pv = image[row, list]
            image[row, list] = 255 - pv
    cv2.imshow("AfterDeal", image)

conv_x, conv_y = prewitt(im)
edge_x = np.abs(conv_x).copy()
edge_y = np.abs(conv_y).copy()
edge_x[edge_x>255] = 255
edge_y[edge_y>255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
edge = edge_y + edge_x
# edge = np.abs(edge_x -edge_y)
edge[edge>255] = 255
edge = edge.astype(np.uint8)
cv2.imshow('edge',edge)
# cv2.imwrite('edge_prewitt.jpg',edge)

#######################
b,g,r = cv2.split(img)
# # z = int((b +g +r) % 3)
# z = b + g + r
new_im = cv2.subtract(edge,r)
# new_im = edge + z
# new_im[new_im>255] = 255
# access_pixels(new_im)
cv2.imshow('merge_pic',new_im)
# new_im = new_im.astype(np.uint8)
#######################
cv2.waitKey(0)
cv2.destroyAllWindows()