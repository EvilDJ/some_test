import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread('./11.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

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
edge = edge_y + edge_x
# edge = np.abs(edge_x -edge_y)
edge[edge>255] = 255
edge = edge.astype(np.uint8)
edge = 255 - edge
cv2.imshow('edge',edge)
cv2.imwrite('edge_scharr.jpg',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()