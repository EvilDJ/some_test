import cv2
import numpy as np
from scipy import signal

im = cv2.imread('./11.jpg')
im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

def roberts(img):
    h,w = img.shape[:2]
    h1, w1 = 2,2
    r1 = np.array([[1,0],[0,-1]], np.float32)
    kr1,kc1 = 0,0
    conr1 = signal.convolve2d(img,r1,mode = 'full',boundary='fill',fillvalue=0)
    conr1 = conr1[h1-kr1-1:h+h1-kr1-1,w1-kc1-1:w+w1-kc1-1]
    r2 = np.array([[0,1],[-1,0]],np.float32)
    kr2, kc2 = 0, 1
    conr2 = signal.convolve2d(img,r2,mode = 'full',boundary='fill',fillvalue=0)
    conr2 = conr2[h1-kr2-1:h+h1-kr2-1,w1-kc2-1:w+w1-kc2-1]
    return (conr1 , conr2)

iconr1,iconr2 = roberts(im)
iconr1 = np.abs(iconr1).astype(np.uint8)
# cv2.imshow('edge_45',iconr1)
iconr2 = np.abs(iconr2).astype(np.uint8)
# cv2.imshow('edge-135',iconr2)
# edge = np.sqrt(np.power(iconr1,2)+np.power(iconr2,2))
edge = iconr2 + iconr1
edge = np.round(edge)
edge[edge>255] = 255
edge = edge.astype(np.uint8)
cv2.imshow('edge',edge)
cv2.imwrite('edge_roberts.jpg',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()