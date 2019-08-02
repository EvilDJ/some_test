from PIL import Image as image#用于改变 图像里的数值
from PIL import ImageEnhance,ImageFilter#包含了Color、Brightness、Contrast和Sharpness
#除常见的模糊、浮雕、轮廓、边缘增强和平滑，还有中值滤波、ModeFilter等
#ImageFilter 包括BLUR,DETAIL Filter函数
im = image.open('F:\pycharm_代码\图像处理/2.jpg')
rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0)#色彩空间转换
# im = im.convert('RGB',rgb2xyz)
enhancer = ImageEnhance.Contrast(im)#Contrast 函数
img = enhancer.enhance(20)
img = ImageEnhance.Sharpness(img)#Sharpness函数
# img = img.enhance(100).show()

im.filter(ImageFilter.BLUR).show()#BLUR, CONTOUR, DETAIL, EMBOSS, MinFilter

'''
· 1 (1-bit pixels, black and white, stored with one pixel per byte)
· L (8-bit pixels, black and white)
· P (8-bit pixels, mapped to any other mode using a colour palette)
· RGB (3x8-bit pixels, true colour)
· RGBA (4x8-bit pixels, true colour with transparency mask)
· CMYK (4x8-bit pixels, colour separation)
· YCbCr (3x8-bit pixels, colour video format)
· I (32-bit signed integer pixels)
· F (32-bit floating point pixels)
'''

