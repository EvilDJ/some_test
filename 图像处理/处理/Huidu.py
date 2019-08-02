from skimage import io
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt

img = io.imread("4.jpg") # (1080, 1920, 3)
# 灰度化
img_gray = rgb2gray(img)  # (1080, 1920)
#二值化
img_binary = np.where(img_gray >= 0.5, 1, 0)  # (1080, 1920)


plt.figure('origin')
plt.imshow(img),plt.axis('off')
plt.figure('gray')
plt.imshow(img_gray),plt.axis('off')
plt.figure('binary')
plt.imshow(img_binary),plt.axis('off')
plt.show()