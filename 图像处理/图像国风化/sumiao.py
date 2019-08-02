import cv2
import numpy as np
from skimage import measure,color,data
import matplotlib.pyplot as plt
from scipy import signal

img = cv2.imread('./3.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def kirsh(img):
    list_edge = []
    k1 = np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]])
    img_k1 = signal.convolve2d(img, k1, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k1))
    k2 = np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])
    img_k2 = signal.convolve2d(img, k2, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k2))
    k3 = np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]])
    img_k3 = signal.convolve2d(img, k3, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k3))
    k4 = np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
    img_k4 = signal.convolve2d(img, k4, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k4))
    k5 = np.array([[-3,-3,5], [-3,0,5],[-3,-3,5]])
    img_k5 = signal.convolve2d(img, k5, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k5))
    k6 = np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
    img_k6 = signal.convolve2d(img, k6, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k6))
    k7 = np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])
    img_k7 = signal.convolve2d(img, k7, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k7))
    k8 = np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
    img_k8 = signal.convolve2d(img, k8, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k8))
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge*(edge>=list_edge[i]) + list_edge[i]*(edge<list_edge[i])
    return edge

def access_pixels(image):
    height, width = image.shape
    # print("width:%s,height:%s,channels:%s" % (width, height))
    for row in range(height):
        for list in range(width):
            pv = image[row, list]
            print(pv)
            if pv > 100:
                image[row, list] = 1
            else:image[row, list] =0
            # image[row, list] = 255 - pv
    return image

edge = kirsh(im)
edge[edge>255]=255
edge = edge.astype(np.uint8)
edge = 255 - edge
cv2.imshow('edge_krish',edge)
# cv2.imwrite('edge_kirsh.jpg',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
