import os
from PIL import Image
import random
import matplotlib.pyplot as plt
from scipy import misc

path_ = r'G:\DATA\VGG_FACE2\vggface2_test\test'
train_l = r'J:\DATA\VGG_face\test_l'
train_r = r'J:\DATA\VGG_face\test_r'
t = open(r'J:\DATA\VGG_face\tes.txt','w')

for i in range(3000):
    if i < 1500:
        t.write('0' + '\n')
    else:
        t.write('1' + '\n')

# dir_name = []
# nl, ml = 0, 0
# for dir_a, dir_n, file_n in os.walk(path_):  # 300
#     if len(file_n) >= 6:
#         # 写匹配数据集的文件
#         num_p = []
#         for i in file_n:
#             im = plt.imread(dir_a + '/' + i)
#             if im.shape[2] == 3:
#                 num_p.append(dir_a + '/' + i)
#         num = random.sample(range(len(num_p)),9)
#         for u in range(3):
#             img1 = Image.open(num_p[(num[u])])
#             img1.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
#             img2 = Image.open(num_p[(num[u + 3])])
#             img2.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
#             dir_name.append(num_p[(num[u + 6])])
#             # t.write('0' + '\n')
#             print(nl, '\t' , '写入到label标签文件下', '0')
#             nl += 1
# for i in range(len(dir_name)):
#     if i < 2997:
#         img1 = Image.open(dir_name[i])
#         img1.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
#         img2 = Image.open(dir_name[i + 3])
#         img2.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
#     else:
#         img1 = Image.open(dir_name[i])
#         img1.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
#         img2 = Image.open(dir_name[i -2997])
#         img2.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
#     print(nl, '\t', '写入到label标签文件下', '1')
#     nl += 1