import os
from PIL import Image
import random
# 从CACD2000面选出三组照片，两张匹配，一张不匹配
# 在筛选4000对做测试集，2000对做匹配集，2000对不匹配对。
path_ = r'G:/DATA/cacd数据集/CACD_shai'
train_l = r'G:/DATA/cacd数据集/train_l'
train_r = r'G:/DATA/cacd数据集/train_r'
train_ = r'G:/DATA/cacd数据集/train_'

dir_name = []
file_name = []
nl, i, j, nr= 0, 0, 0, 0
for dir_a, dir_n, file_n in os.walk(path_):
    dir_name.append(dir_a)
dir_name = dir_name[1:]
for i in range(len(dir_name)):
    dir = dir_name[i]
    if i == 299:
        dir_ = dir_name[0]
    if i <= 298:
        dir_ = dir_name[i+1]
    print(dir)
    for dir_a, dir_n, file_n in os.walk(dir):
        num = random.sample(range(len(file_n)), 41)
        for u in range(0, 40):
            if u == 40:
                img1 = Image.open(dir + '/' + file_n[(num[0])])
                img1.save(train_l + '/' + 'pair_l_' + str(nl) + '.jpg')
            if u<=39:
                img1 = Image.open(dir + '/' + file_n[(num[u + 1])])
                img1.save(train_l + '/' + 'pair_l_' + str(nl) + '.jpg')
            print(str(nl) + '.jpg' + 'save to pair_l_')
            img2 = Image.open(dir + '/' + file_n[(num[u])])
            img2.save(train_ + '/' + 'pair_' + str(nl) + '.jpg')
            print(str(nl) + '.jpg' + 'save to pair_')
            nl += 1
    print(dir_)
    for dir_a, dir_n, file_r in os.walk(dir_):
        num = random.sample(range(len(file_r)), 40)
        for u in range(0, 40):
            img3 = Image.open(dir_ + '/' + file_r[(num[u])])
            img3.save(train_r + '/' + 'pair_r_' + str(nr) + '.jpg')
            print(str(nr) + '.jpg' + 'save to pair_r_')
            nr += 1