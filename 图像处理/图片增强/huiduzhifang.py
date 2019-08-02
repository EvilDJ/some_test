import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import signal
from skimage.feature import hog,local_binary_pattern

def calc(img):
    row,col = img.shape
    grayHist = np.zeros([256],np.uint64)
    for r in range(row):
        for c in range(col):
            grayHist[img[r][c]] += 1
    return grayHist

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

def hog_lbp(img):
    # img.astype(np.int32)
    _,hog_img = hog(img,orientations=9,pixels_per_cell=(8,8),cells_per_block=(8,8),visualise=True)
    lbp = local_binary_pattern(img, 8 ,1)
    img = lbp + hog_img
    return img

img1 = cv2.imread('./1.jpg')
img2 = cv2.imread('./2.jpg')
img3 = cv2.imread('./3.jpg')
img_1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img_2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img_3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

img_1_r = robin(img_1)
img_2_r = robin(img_2)
img1_2_r = abs(img_1_r - img_2_r)
img1_2_r[img1_2_r>255] = 255
gray_r = calc(img1_2_r)

img_1_l = hog_lbp(img_1)
img_2_l = hog_lbp(img_2)
img1_2_l = abs(img_1_l - img_2_l)
img1_2_l = img1_2_l.astype(np.int32)
img1_2_l[img1_2_l>255] = 255
gray_l = calc(img1_2_l)

# img_1_l = robin(img_1)
# img_2_l = robin(img_3)
# img1_2_l = abs(img_1_l - img_2_l)
# img1_2_l = img1_2_l.astype(np.int32)
# img1_2_l[img1_2_l>255] = 255
# gray_l = calc(img1_2_l)

plt.plot(range(256),gray_r,'.',linewidth = 1 ,c = 'black',label='Robinson')
plt.plot(range(256),gray_l,'-',linewidth = 1 ,c = 'red',label ='LBP+HOG')
plt.xlabel('Grayscale Value')
plt.ylabel('Quantity')
plt.legend(loc=1)
plt.title("Histogram of similar graphs under Robinson and LBP+HOG")
plt.show()