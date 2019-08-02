from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import math

# settings for LBP
radius = 1  # LBP算法中范围半径的取值
n_points = 8 * radius # 领域像素点数

img = cv2.imread('./1.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
lbp = local_binary_pattern(im,n_points,radius)

plt.imshow(im)
plt.show()