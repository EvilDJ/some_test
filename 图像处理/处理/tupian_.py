from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2


image = Image.open('F:\pycharm_代码\图像处理/2.jpg')
image1=np.array(image)
#图片的分割框
box=(256,256,1000,800)
data = np.array(image.crop(box))
data_ = cv2.resize(data,(1200,1200))

# rows,cols,dims=data.shape
# for i in range(5000):
#     x=np.random.randint(0,rows)
#     y=np.random.randint(0,cols)
#     data[x,y,:]= 255

print(image1.shape)
plt.imshow(image1)
# print(data.shape)
# print(data)
plt.figure("image")
plt.subplot(1,2,1), plt.title('origin')
plt.imshow(image), plt.axis('off')
plt.subplot(1,2,2), plt.title('chuli')
plt.imshow(data_), plt.axis('off')
plt.show()


