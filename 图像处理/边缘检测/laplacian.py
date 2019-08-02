import cv2
import numpy as np
import math
from scipy import signal

img = cv2.imread('./4.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def laplacia(image, _bou='fill'):
    kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
    i_conv_lap = signal.convolve2d(image,kernel,mode='same',boundary=_bou,fillvalue=0)
    return i_conv_lap

i_conv_lap = laplacia(im,'symm')
asb = np.copy(i_conv_lap)
# asb = asb.astype(np.float32)
# asb[asb>=0] = 1
# asb[asb<0] = 1.0 + np.tanh(asb[asb<0])
asb[asb>=0] = 255
asb[asb<0] = 0
asb = asb.astype(np.uint8)
cv2.imshow('asb',asb)
cv2.imwrite('edge_laplacian.jpg',asb)
cv2.waitKey(0)
cv2.destroyAllWindows()
