#CACD2000的所有图片按照名字进行分开存放
import makdir as mk
import os
from PIL import Image

path = 'F:/网络数据集/cacd数据集/cacd_all'
path_ = 'F:/网络数据集/cacd数据集/CACD2000'

#dir_a 文件路径名字符串，file_n 图片的名字列表
for dir_a, dir_n, file_n in os.walk(path):
    #print(dir_a)
    # print(dir_n)
    # print(file_n)
    num = 0
    for fln in file_n:
        img = Image.open(path +'/'+ fln)
        #print(fln)
        strl = fln[3:-9]
        #print(str)
        path_name = path_ + "/" + strl
        #print(path_name)
        mk.mkdir(path_name)
        img.save(path_name + '/' + strl + '_'+ str(num) + '.jpg')
        num += 1
# for dr_a, di_n,fil_n in os.walk(path_):
#     n = 0
#     for