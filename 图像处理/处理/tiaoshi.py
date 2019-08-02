from skimage import io
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import cv2

'''
img = io.imread("2.jpg")  # (1080, 1920, 3)

io.imshow(img)
io.show()
print(img)

[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ..., 
  [217 224 234]
  [217 224 234]
  [217 224 234]]
  ..., 
 [[188 165 131]
  [195 175 140]
  [186 166 131]
  ..., 
  [163 138 108]
  [156 131 101]
  [153 128  98]]]


# 灰度化
img_gray = rgb2gray(img)  # (1080, 1920)

io.imshow(img_gray)
io.show()
print(img_gray)

[[ 1.          1.          1.         ...,  0.87542549  0.87542549
   0.87542549]
 [ 1.          1.          1.         ...,  0.85973922  0.85973922
   0.85973922]
 [ 1.          1.          1.         ...,  0.86366078  0.86366078
   0.86366078]
 ..., 
 [ 0.64347137  0.6277851   0.71405961 ...,  0.66333137  0.67901765
   0.7103902 ]
 [ 0.57931961  0.62637843  0.70286039 ...,  0.6594098   0.62411569
   0.60450784]
 [ 0.65661216  0.6930451   0.65775098 ...,  0.55352745  0.52607647
   0.51431176]]

img_binary = np.where(img_gray >= 0.5, 1, 0)  # (1080, 1920)

print(img_binary)

[[1 1 1 ..., 1 1 1]
 [1 1 1 ..., 1 1 1]
 [1 1 1 ..., 1 1 1]
 ...,
 [1 1 1 ..., 1 1 1]
 [1 1 1 ..., 1 1 1]
 [1 1 1 ..., 1 1 1]]


io.imshow(img_binary)
io.show()
'''


img = io.imread("2.jpg") # (1080, 1920, 3)
h = img.shape[0]
w = img.shape[1]
factor_count = 0
minsize = 20
minl=np.amin([h, w])
m=12.0/minsize
minl=minl*m

scales=[]
while minl>=0.5:
    print('minl=',minl)
    scales += [m*np.power(0.709, factor_count)]
    minl = minl*0.709
    factor_count += 1


for scale in scales:
    print('scale = ', scale)
    hs = int(np.ceil(h * scale))
    ws = int(np.ceil(w * scale))
    img_data = cv2.resize(img, (hs, ws))
    img_data = (img_data - 127.5) * 0.0078125
    print('img_data:',img_data)
    img_x = np.expand_dims(img_data,0)
    print('img_x:',img_x)
    img_y = np.transpose(img_x, (0, 2, 1, 3))
    print('img_y=',img_y)
    # print('img:', img.shape)
    # print('img_data:', img_data.shape)
    # print(img_data)
    # plt.imshow(img_data)
    # plt.show()


# 灰度化
# img_gray = rgb2gray(img)  # (1080, 1920)
# #二值化
# img_binary = np.where(img_gray >= 0.5, 1, 0)  # (1080, 1920)
# plt.imshow(img_binary)
# plt.show()
#
# plt.figure("图像")
# plt.subplot(1,3,1), plt.title('origin')
# plt.imshow(img),plt.axis('off')
# plt.subplot(1,3,2), plt.title('gray')
# plt.imshow(img_gray),plt.axis('off')
# plt.subplot(1,3,3), plt.title('binary')
# plt.imshow(img_binary),plt.axis('off')
# plt.show()