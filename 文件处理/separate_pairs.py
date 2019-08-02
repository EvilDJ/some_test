import os

#一系列路径参数
list = []#txt文件每行生成list表
path = r"F:/网络数据集/lfw/lfw"#总图片路径
#tra_txt = "F:/网络数据集/lfw/pairsDevTrain.txt"#总训练集txt文件
#tes_txt = "F:/网络数据集/lfw/pairsDevTest.txt"
#tr_p1 = open(r'F:\网络数据集\lfw\tra_pairs_1.txt','w')#训练集 的 左图
#tr_p2 = open(r'F:\网络数据集\lfw\tra_pairs_2.txt','w')#训练集 的 右图（包含匹配与不匹配对象）
te_p1 = open(r'F:\网络数据集\lfw\test_l.txt','w')
te_p2 = open(r'F:\网络数据集\lfw\test_r.txt','w')
#tr_p1.close()
#tr_p2.close()
#匹配，标签为0；不匹配，标签为1.
count = 0
num_l= 0
num_r=0
with open(r'F:/网络数据集/lfw/pairsDevTest.txt', 'r') as f:
    for line in f:
        count = count + 1
        line = line.strip()
        line = line.replace('\t',' ')
        list = line.split(" ")
        print(list)
        # 文件夹下文件夹的路径 字符串型，文件夹的名字，文件夹内的文件名字 list表型
        for dir_a, dir_n, file_n in os.walk(path):
            if file_n != []:
                if len(list) == 3:
                    # if dir_a.count(list[0]) >0:
                    if dir_a.find(list[0], 16, 17 + len(list[0])) > 0 and len(dir_a) == 17 + len(list[0]):
                        for i, val in enumerate(file_n):
                            print("--------")
                            # print(i,list[1],list[2])
                            # print(val)
                            if int(list[1]) == (i + 1):
                                num_l = num_l + 1
                                print("将" + val + "写入train_l.txt下！")
                                te_p1.write('0' +'\n')
                            if int(list[2]) == (i + 1):
                                num_r = num_r + 1
                                print("将" + val + "写入train_r.txt下！")
                                te_p2.write('0' +'\n')
                    #else:
                       #print("/\/\/\/\/\/\/")
                        #continue
                        # name = name + "01" + '\n'
                elif len(list) == 4:
                    if dir_a.find(list[0], 16, 17 + len(list[0])) > 0 and len(dir_a) == 17 + len(list[0]):
                        for i, val in enumerate(file_n):
                            print('===========')
                            if (i + 1) == int(list[1]):
                                num_l = num_l + 1
                                print("将" + val + "写入train_l.txt下！")
                                te_p1.write('1'+'\n')
                                print("*************")
                            #else:
                                #print("#############")
                                #continue
                    if dir_a.find(list[2], 16, 17 + len(list[2])) > 0 and len(dir_a) == 17 + len(list[2]):
                        for i, val in enumerate(file_n):
                            print('+++++++++++')
                            if (i + 1) == int(list[3]):
                                print("将" + val + "写入train_r.txt下！")
                                num_r = num_r + 1
                                te_p2.write('1'+'\n')
                                print("^^^^^^^^^^^")
                            #else:
                               #
                                #continue
    te_p1.close()
    te_p2.close()
    print("总共遍历了：", count, "次")
    print('num_r = ',num_r,'\nnum_l = ',num_l)
