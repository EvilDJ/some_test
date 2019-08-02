import cv2

img = cv2.imread('./3.jpg')
im_ = cv2.imread('./4.jpg')
print(img.shape)
print(im_.shape)
img = cv2.resize(im_,img.shape[:2])
cv2.imshow('img',img)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()