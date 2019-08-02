import cv2
import numpy as np

img = cv2.imread('./3.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# a = 8
# im = float(a) * img + 2
row ,col = img.shape
im = np.zeros([row, col], np.uint64)
for r in range(row) :
    for c in range(col) :
        if img[r][c] <50:
            im[r][c] = 0.5*img[r][c]
        elif img[r][c] >= 50 and img[r][c] < 150:
            im[r][c] = 3.6*img[r][c] - 310
        else:im[r][c] = 0.238*img[r][c]+194
im[im>255] = 255
im = np.round(im)
im = im.astype(np.uint8)
cv2.imshow('im',im)
cv2.waitKey(0)
cv2.destroyAllWindows()