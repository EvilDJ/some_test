import os
from PIL import Image
import random
import matplotlib.pyplot as plt
from scipy import misc

# 从CACD数据集中随机筛选16000对，8000对是匹配集，8000对不匹配。
# 在筛选4000对做测试集，2000对做匹配集，2000对不匹配对。
path_ = r'F:/网络数据集/cacd数据集/CACD_shai'
train_l = r'F:/网络数据集/cacd数据集/train_l'
train_r = r'F:/网络数据集/cacd数据集/train_r'
te_p1 = open(r'F:/网络数据集/cacd数据集/train.txt', 'w')  # 对应label标签文件

dir_name = []
nl, i = 0, 0
for dir_a, dir_n, file_n in os.walk(path_):  # 300
    # 筛选8000对的训练集
    if len(file_n) >= 40:
        # 写匹配数据集的文件
        num = random.sample(range(len(file_n)), 10)
        # 在file_n的范围内，生成4个不相等的数字
        # num_m = len(num)/2
        for u in range(5):
            img1 = Image.open(dir_a + '/' + file_n[(num[u])])
            img1.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
            img2 = Image.open(dir_a + '/' + file_n[(num[u + 5])])
            img2.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
            te_p1.write('0' + '\n')
            print(nl, '\t', file_n[(num[u])], file_n[(num[u + 5])], '写入到label标签文件下', '0')
            nl += 1
        # img3 = Image.open(dir_a + '/' + file_n[(num[2])])
        # img3.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
        # img4 = Image.open(dir_a + '/' + file_n[(num[3])])
        # img4.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
        # te_p1.write('0' + '\n')
        # print(nl,'\t',file_n[(num[2])], file_n[(num[3])], '写入到label标签文件下', '0')
        # nl += 1
        # img5 = Image.open(dir_a + '/' + file_n[(num[4])])
        # img5.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
        # img6 = Image.open(dir_a + '/' + file_n[(num[5])])
        # img6.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
        # te_p1.write('0' + '\n')
        # print(nl, '\t', file_n[(num[4])], file_n[(num[5])], '写入到label标签文件下', '0')
        # nl += 1
        # img7 = Image.open(dir_a + '/' + file_n[(num[6])])
        # img7.save(train_l + '/' + 'pairl_' + str(nl) + '.jpg')
        # img8 = Image.open(dir_a + '/' + file_n[(num[7])])
        # img8.save(train_r + '/' + 'pairr_' + str(nl) + '.jpg')
        # te_p1.write('0' + '\n')
        # print(nl, '\t', file_n[(num[6])], file_n[(num[7])], '写入到label标签文件下', '0')
        # nl += 1
        # 写不匹配数据集的文件
        file_name = []
        mum = random.sample(range(len(file_n)), 40)
        for m in range(20):
            file_name.append(dir_a + '/' + file_n[(mum[m])])
            file_name.append(dir_a + '/' + file_n[(mum[m + 20])])
        dir_name.append(file_name)
#         print('file_name:',len(file_name))
# print('dir_name:',len(dir_name))
# dir_name.append([dir_a + '/' + file_n[(mum[0])],dir_a + '/' + file_n[(mum[1])],
#                  dir_a + '/' + file_n[(mum[2])],dir_a + '/' + file_n[(mum[3])],
#                  dir_a + '/' + file_n[(mum[4])],dir_a + '/' + file_n[(mum[5])],
#                  dir_a + '/' + file_n[(mum[6])],dir_a + '/' + file_n[(mum[7])]])
tl = 1500
for j in range(len(dir_name)):
    if j != 299:
        for x in range(5):
            img1_l = Image.open(dir_name[j][x])
            img1_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
            img1_r = Image.open(dir_name[j + 1][x + 5])
            img1_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
            te_p1.write('1' + '\n')
            print(tl, '\t', dir_name[j][x], dir_name[j + 1][x], '写入到label标签文件下', '1')
            tl += 1
        # img1_l = Image.open(dir_name[j][0])
        # img1_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img1_r = Image.open(dir_name[j + 1][4])
        # img1_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl,'\t',dir_name[j][0], dir_name[j + 1][4], '写入到label标签文件下', '1')
        # tl += 1
        # img2_l = Image.open(dir_name[j][1])
        # img2_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img2_r = Image.open(dir_name[j + 1][5])
        # img2_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl,'\t',dir_name[j][1], dir_name[j + 1][5], '写入到label标签文件下', '1')
        # tl += 1
        # img3_l = Image.open(dir_name[j][2])
        # img3_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img3_r = Image.open(dir_name[j + 1][6])
        # img3_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl, '\t', dir_name[j][2], dir_name[j + 1][6], '写入到label标签文件下', '1')
        # tl += 1
        # img4_l = Image.open(dir_name[j][3])
        # img4_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img4_r = Image.open(dir_name[j + 1][7])
        # img4_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl, '\t', dir_name[j][3], dir_name[j + 1][7], '写入到label标签文件下', '1')
        # tl += 1
    if j == 299:
        for x in range(5):
            img1_l = Image.open(dir_name[j][x])
            img1_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
            img1_r = Image.open(dir_name[0][x + 5])
            img1_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
            te_p1.write('1' + '\n')
            print(tl, '\t', dir_name[j][x], dir_name[0][x + 5], '写入到label标签文件下', '1')
            tl += 1
        # img1 = Image.open(dir_name[j][0])
        # img1.save(train_l + '/' + 'pairl_' + str(15999) + '.jpg')
        # img2 = Image.open(dir_name[0][0])
        # img2.save(train_r + '/' + 'pairr_' + str(15999) + '.jpg')
        # te_p1.write('1' + '\n')
        # print('15999',dir_name[j][0], dir_name[0][0], '写入到label标签文件下', '1')
        # img3 = Image.open(dir_name[j][1])
        # img3.save(train_l + '/' + 'pairl_' + str(16000) + '.jpg')
        # img4 = Image.open(dir_name[0][1])
        # img4.save(train_r + '/' + 'pairr_' + str(16000) + '.jpg')
        # te_p1.write('1' + '\n')
        # print('16000',dir_name[j][1], dir_name[0][1], '写入到label标签文件下', '1')
        # img1_l = Image.open(dir_name[j][0])
        # img1_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img1_r = Image.open(dir_name[0][4])
        # img1_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl, '\t', dir_name[j][0], dir_name[0][4], '写入到label标签文件下', '1')
        # tl += 1
        # img2_l = Image.open(dir_name[j][1])
        # img2_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img2_r = Image.open(dir_name[0][5])
        # img2_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl, '\t', dir_name[j][1], dir_name[0][5], '写入到label标签文件下', '1')
        # tl += 1
        # img3_l = Image.open(dir_name[j][2])
        # img3_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img3_r = Image.open(dir_name[0][6])
        # img3_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl, '\t', dir_name[j][2], dir_name[0][6], '写入到label标签文件下', '1')
        # tl += 1
        # img4_l = Image.open(dir_name[j][3])
        # img4_l.save(train_l + '/' + 'pairl_' + str(tl) + '.jpg')
        # img4_r = Image.open(dir_name[0][7])
        # img4_r.save(train_r + '/' + 'pairr_' + str(tl) + '.jpg')
        # te_p1.write('1' + '\n')
        # print(tl, '\t', dir_name[j][3], dir_name[0][7], '写入到label标签文件下', '1')
#
# # print(dir_name)
# # img = misc.imread(dir_name[0][1])
# # plt.imshow(img)
# # plt.show()
te_p1.close()
