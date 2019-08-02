import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread('./3.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def laplacia(image, _bou='fill'):
    # kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
    nkernel = np.array([[0,1,0],[1,-4,1],[0,1,0]],np.float32)
    mkernel = np.array([[2,0,2],[0,-8,0],[2,0,2]],np.float32)
    i_conv_lap = signal.convolve2d(image,mkernel,mode='same',boundary=_bou,fillvalue=0)
    # i_conv_lap = signal.convolve2d(i_conv_lap,nkernel,mode='same',boundary=_bou,fillvalue=0)
    return i_conv_lap


i_conv_lap = laplacia(im,'symm')
asb = np.copy(i_conv_lap)
asb = asb.astype(np.float32)
asb[asb>=0] = 125
asb[asb<0] = 125 *(1-np.tanh(asb[asb<0]))

asb = asb.astype(np.uint8)
asb = 255 -asb
cv2.imshow('asb',asb)
# cv2.imwrite('edge_laplacian.jpg',asb)
cv2.waitKey(0)
cv2.destroyAllWindows()
