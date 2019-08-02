import cv2
import numpy as np

img = cv2.imread('./3.jpg')
ima = np.max(img)
imi = np.min(img)
omi,oma = 0,255

a = float(oma - omi)/(ima - imi)
b = oma - a * ima
o = a * img + b
o = o.astype(np.uint8)
cv2.imshow('o',o)
cv2.waitKey(0)
cv2.destroyAllWindows()