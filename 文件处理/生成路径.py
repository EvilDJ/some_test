import os
list = []
path = r"F:/网络数据集/lfw/lfw"
pair_txt = open(r'F:\网络数据集\lfw\match_pair.txt','w')#train and test 's list
unpair_txt = open(r'F:\网络数据集\lfw\nomatch_pair.txt','w')

count = 0
with open(r'F:/网络数据集/lfw/pairsDevTrain.txt', 'r') as f:
    for line in f:
        count = count + 1
        line = line.strip()
        line = line.replace('\t',' ')
        list = line.split(" ")
        print(list)
        name = ""
        # 获得文件下的文件名称
        # 文件夹下文件夹的路径 字符串型，文件夹的名字，文件夹内的文件名字 list表型
        for dir_a, dir_n, file_n in os.walk(path):
            if  file_n != []:
                if len(list) == 3:
                    #if dir_a.count(list[0]) >0:
                    if dir_a.find(list[0],16,17+len(list[0])) >0 and len(dir_a) == 17+len(list[0]) :
                        for i,val in enumerate(file_n):
                            print("-----------")
                            #print(i,list[1],list[2])
                            #print(val)
                            if int(list[1]) == (i+1) or int(list[2]) == (i+1) :
                                print("匹配对象"+ str(list) +"写入match_pair.txt下！")
                                name = "/0/" + val + '  '
                                pair_txt.write(name)
                            else:
                                continue
                        #name = name + "01" + '\n'
                        pair_txt.write('\n')
                elif len(list) == 4:
                    if dir_a.find(list[0], 16, 17 + len(list[0])) > 0 and len(dir_a) == 17+len(list[0]):
                        for i,val in enumerate(file_n):
                            print('===========')
                            if (i+1) == int(list[1]) :
                                name = "/1/" + val + '  '
                                unpair_txt.write(name)
                                print("不匹配对象1" + str(list) + "写入nomatch_pair.txt下！")
                            else:
                                continue
                    if dir_a.find(list[2], 16, 17 + len(list[2])) > 0 and len(dir_a) == 17+len(list[2]):
                        for i,val in enumerate(file_n):
                            print('+++++++++++')
                            if (i+1) == int(list[3]) :
                                name = "/1/" + val + '  '
                                unpair_txt.write(name)
                                print("不匹配对象2" + str(list) + "写入nomatch_pair.txt下！")
                            else:
                                continue
                        #name = name + "10" + '\n'
                        unpair_txt.write('\n')
    unpair_txt.close()
    pair_txt.close()
    print("总共遍历了：",count,"次")
