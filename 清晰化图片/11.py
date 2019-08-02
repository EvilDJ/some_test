from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2

imagefile= cv2.imread("wx.jpg")

odd_numbers_lines = []
even_numbers_lines =[]
count_lines =1
while count_lines <=imagefile.shape[0]:
    if count_lines %2 !=0:
        odd_numbers_lines.append(imagefile[count_lines-1])
        count_lines += 1
    if count_lines %2 == 0:
            even_numbers_lines.append(imagefile[count_lines-1])
            count_lines += 1
            
#if countodd_numbers_lines = [imagefile[count_lines] for count_lines in range(imagefile.shape[0]) _lines % 2 != 0]


even_numbers_lines = [imagefile[count_lines] for count_lines in range(imagefile.shape[0]) if count_lines % 2 == 0]
plt.imshow(even_numbers_lines)
plt.show()