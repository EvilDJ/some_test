from skimage.feature import hog
import matplotlib.pyplot as plt
import cv2
from skimage.feature import local_binary_pattern

# settings for LBP
radius = 1  # LBP算法中范围半径的取值
n_points = 8 * radius # 领域像素点数

img = cv2.imread('./1.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

normalised_blocks, hog_image = hog(im, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(8, 8), visualise=True)
lbp = local_binary_pattern(im,n_points,radius)

im = hog_image + lbp

plt.imshow(im)
plt.show()