import os
from PIL import Image
import random
import matplotlib.pyplot as plt
from scipy import misc

# 从CACD数据集中随机筛选16000对，8000对是匹配集，8000对不匹配。
# 在筛选4000对做测试集，2000对做匹配集，2000对不匹配对。
path_ = r'G:\DATA\VGG_FACE2\vggface2_train\train'
train_l = r'J:\DATA\VGG_face\train_l'
train_r = r'J:\DATA\VGG_face\train_r'
train_ = r'J:\DATA\VGG_face\train'
t = open(r'J:\DATA\VGG_face\tra.txt','w')

dir_name = []
nl, ml = 0, 0
for dir_a, dir_n, file_n in os.walk(path_):  # 300
    if len(file_n) >= 60:
        # 写匹配数据集的文件
        num_p = []
        for i in file_n:
            im = plt.imread(dir_a + '/' + i)
            if im.shape[2] == 3:
                num_p.append(dir_a + '/' + i)
        num = random.sample(range(len(num_p)),60)
        for u in range(20):
            # img1 = Image.open(num_p[(num[u])])
            # img1.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
            img3 = Image.open(num_p[(num[u + 20])])
            img3.save(train_ + '/' + 'pair__' + str(nl) + '.jpg')
            # dir_name.append(num_p[(num[u + 40])])
            # t.write('0' + '\n')
            print(nl, '\t' , '写入到label标签文件下', '0')
            nl += 1
# for i in dir_name:
#     if ml < 20 :
#         img1 = Image.open(i)
#         img1.save(train_r + '/' + 'pairr_' + str(ml + 12380) + '.jpg')
#     else:
#         img1 = Image.open(i)
#         img1.save(train_r + '/' + 'pairr_' + str(ml - 20) + '.jpg')
#     print(ml, '\t', '写入到label标签文件下', '1')
#     ml += 1
