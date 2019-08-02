import cv2
import numpy as np
from scipy import signal

img = cv2.imread('./4.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

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

def robin(img):
    list_edge = []
    k1 = np.array([[1,1,1],[1,-2,1],[-1,-1,-1]])
    img_k1 = signal.convolve2d(img, k1, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k1))
    k2 = np.array([[1,1,1],[-1,-2,-1],[-1,-1,1]])
    img_k2 = signal.convolve2d(img, k2, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k2))
    k3 = np.array([[-1,1,1],[-1,-2,1],[-1,1,1]])
    img_k3 = signal.convolve2d(img, k3, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k3))
    k4 = np.array([[-1,-1,1],[-1,-2,1],[1,1,1]])
    img_k4 = signal.convolve2d(img, k4, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k4))
    k5 = np.array([[-1,-1,-1],[1,-2,1],[1,1,1]])
    img_k5 = signal.convolve2d(img, k5, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k5))
    k6 = np.array([[1,-1,-1],[1,-2,-1],[1,1,1]])
    img_k6 = signal.convolve2d(img, k6, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k6))
    k7 = np.array([[1,1,-1],[1,-2,-1],[1,1,-1]])
    img_k7 = signal.convolve2d(img, k7, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k7))
    k8 = np.array([[1,1,1],[1,-2,-1],[1,-1,-1]])
    img_k8 = signal.convolve2d(img, k8, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k8))
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge*(edge>=list_edge[i]) + list_edge[i]*(edge<list_edge[i])
    return edge

edge_robin = robin(im)
edge_robin[edge_robin>255]=255
edge_robin = edge_robin.astype(np.uint8)

# (_, thresh) = cv2.threshold(im, 90, 255, cv2.THRESH_BINARY)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# closed = cv2.erode(closed, None, iterations=4)
# closed = cv2.dilate(closed, None, iterations=4)

prewitt_x,prewitt_y = prewitt(im)
prewitt_x[prewitt_x>255] = 255
prewitt_y[prewitt_y>255] = 255
prewitt_x = prewitt_x.astype(np.uint8)
prewitt_y = prewitt_y.astype(np.uint8)

robert_x,robert_y = roberts(im)
robert_x = np.abs(robert_x).astype(np.uint8)
robert_y = np.abs(robert_y).astype(np.uint8)

edge = prewitt_x + robert_y
edge[edge>255] = 255
edge = edge.astype(np.uint8)

cv2.imshow('edge',edge)
# cv2.imwrite('merge_0.jpg',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()