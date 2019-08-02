import os

path_ = r'G:\DATA\OTB100\OTB100\OTB100'
csv_path = 'G:\DATA\OTB100\OTB100'
ground = 'groundtruth_rect.txt'
txt = []
for dir_a, dir_n, file_n in os.walk(path_):
    if 'img' not in dir_a and 'G:\DATA\OTB100\OTB100\OTB100' != dir_a:
        if 'Skating2' not in dir_a:
            txt.append(dir_a + '\\' + ground)
            print(dir_a + '\\' + ground)

l = 0
for i in txt:
    csv = csv_path + '\\' + str(l) +'.csv'
    cdd = open(csv, 'w')
    num = 0
    with open(i, 'r') as f:
        for s in f:
            if '\t' in s:
                s = s.replace('\t', ',')
            print(s)
            cdd.write(str(num) + ',' + s)
            num += 1
    cdd.closed
    num = 0
    l += 1