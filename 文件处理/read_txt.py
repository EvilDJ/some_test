list = []
with open('F:/网络数据集/lfw/测试/33.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.replace('\t' ,' ')
        list = line.split(" ")
        print(list)
        print(len(list))
        print(list[2])
        
        #print(len(list))
        '''
        name = []
        numb = []
        for i in list:
            if bool(re.search('[a-z]', i)) == True:
                name.append(i)
            if bool(re.search('[0-300]', i)) == True:
                numb.append(i)

        #print(name)
        #print(numb)
        '''
