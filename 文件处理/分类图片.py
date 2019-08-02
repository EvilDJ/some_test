import os
from PIL import Image

list = []
path = r"F:/网络数据集/lfw/lfw"
tra_r = r"F:/网络数据集/lfw/test_r/"#存放匹配对象
tra_l = r"F:/网络数据集/lfw/test_l/"#存放不匹配对象
count = 0
num_l=0
num_r=0
with open(r'F:/网络数据集/lfw/pairsDevTest.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.replace('\t',' ')
        list = line.split(" ")
        print(list)
        # 获得文件下的文件名称
        # 文件夹下文件夹的路径，文件夹的名字，文件夹内的文件名字
        for dir_a, dir_n, file_n in os.walk(path):
            if  file_n != []:
                if len(list) == 3:
                    #if dir_a.count(list[0]) >0:
                    if dir_a.find(list[0],16,17+len(list[0])) >0 and len(dir_a) == 17+len(list[0]) :
                        for i,val in enumerate(file_n):
                            print("-----------")
                            #print(i,list[1],list[2])
                            #print(val)
                            if int(list[1]) == (i+1) :
                                num_l += 1
                                fl = dir_a + '/' + val
                                img = Image.open(fl)
                                for new_d,new_dn,new_f in os.walk(tra_l):
                                    if ('pairl_' + str(num_l) +'.jpg') not in new_f:
                                        img.save(tra_l + '/' + 'pairl_' + str(num_l) +'.jpg')
                                    else:continue
                            if int(list[2]) == (i+1) :
                                num_r += 1
                                fr = dir_a + '/' +val
                                img = Image.open(fr)
                                for n_d,n_dn,n_f in os.walk(tra_r):
                                    if ('pairr_' + str(num_r) +'.jpg') not in n_f:
                                        img.save(tra_r + '/' + 'pairr_' + str(num_r) +'.jpg')
                                    else:continue
                                    
                                    
                        '''
                            if int(list[1]) == (i+1) or int(list[2]) == (i+1) :
                                print('+++++++++++')
                                f1 = dir_a+ '/' + val
                                img = Image.open(f1)
                                for new_d, new_dn, new_f in os.walk (tra_01):
                                    if val not in new_f:
                                       img.save(tra_01 + '/' + val)
                                       print('***********')
                                    else:
                                        continue
                            else:
                                print('%%%%%%%%%%%')
                                continue
                        ###
                        for fg in range(1,len(file_n)+1):
                            print(fg)
                            if list[1] == fg or list[2] == fg:
                                print('---------')
                                f1 = dir_a + '/' + file_n[f]
                                img = Image.open(f1)
                                #img.save(tra_01 + '/' + file_n[f])
                                for n_d,n_dn,n_f in os.walk(tra_01):
                                    if n_f == file_n[fg] :
                                        continue

                                    else:
                                        img.save(tra_01 + '/' + file_n[fg])
                        '''
                elif len(list) == 4:
                    if dir_a.find(list[0], 16, 17 + len(list[0])) > 0 and len(dir_a) == 17+len(list[0]):
                        for i,val in enumerate(file_n):
                            if (i+1) == int(list[1]) :
                                num_l += 1
                                f1 = dir_a + '/' + val
                                img = Image.open(f1)
                                for nw_d, nw_dn, nw_f in os.walk(tra_l):
                                    if ('pairl_'+ str(num_l) +'.jpg') not in nw_f:
                                        img.save(tra_l + '/' + 'pairl_'+ str(num_l) +'.jpg')
                                        print('1###########')
                                    else:
                                        continue
                            else:
                                print('1==========')
                                continue
                    if dir_a.find(list[2], 16, 17 + len(list[2])) > 0 and len(dir_a) == 17+len(list[2]):
                        for i,val in enumerate(file_n):
                            if (i+1) == int(list[3]) :
                                num_r += 1
                                f1 = dir_a + '/' + val
                                img = Image.open(f1)
                                for nw_d, nw_dn, nw_f in os.walk(tra_r):
                                    if str('pairr_'+ str(num_r) +'.jpg') not in nw_f:
                                        img.save(tra_r + '/' + 'pairr_'+ str(num_r) +'.jpg')
                                        print('2###########')
                                    else:
                                        continue
                            else:
                                print('2==========')
                                continue
        count = count + 1
    print("总共遍历了：",count,"次")
    print('num_l=',num_l,'\nnum_r=',num_r)
    '''
                    
                    
                    if dir_a.count(list[0]) or dir_a.count(list[2]) >0:
                        print('!!!!!!!!!!!!!!!!')
                        print(list[0],list[2])
                        print(dir_a)
                        for i, val in enumerate(file_n):
                            print(file_n)
                            if (i+1) == int(list[1]) or (i+1) == int(list[3]):
                                f1 = dir_a +'/' + val
                                img = Image.open(f1)
                                for nw_d, nw_dn, nw_f in os.walk(tra_10):
                                    if val not in nw_f:
                                       img.save(tra_10 + '/' + val)
                                       print('###########')
                                    else:
                                        break
                            else:
                                print('==========')
                                break
                    
                    
                
                
                
                for f in file_n:
                    f1 = dir_a + '/' + f
                    img = Image.open(f1)
                    img.save(tra_01 + '/' + f)
                
        #for dir in os.listdir(path):
    '''
    
    
    
    
    
    
    
    
    
    
    


    

    