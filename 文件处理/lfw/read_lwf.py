import makdir as mk
import os
from PIL import Image

path = 'G:/DATA/VGG_FACE2/vggface2_test/test'
path_ = 'F:/网络数据集/cacd数据集/CACD2000'

m = 1
for dir_a, dir_n, file_n in os.walk(path):
    if len(file_n) > 1:
        print(dir_a)
        m += 1
    # print(dir_a,len(file_n))
print(m)
    # num = 0
    # for fln in file_n:
    #     img = Image.open(path +'/'+ fln)
    #     #print(fln)
    #     strl = fln[3:-9]
    #     #print(str)
    #     path_name = path_ + "/" + strl
    #     #print(path_name)
    #     mk.mkdir(path_name)
    #     img.save(path_name + '/' + strl + '_'+ str(num) + '.jpg')
    #     num += 1