import os
import re


def replaceDirName(rootDir):
    dirs = os.listdir(rootDir)
    r = 0
    for dir in dirs:
        print('oldname is:' + dir)  # 输出老的名字
        # string = dir.split('、')
        # num = string[0]
        # temp = "%03d" % int(num) + '-' + string[1]  # 主要目的是在数字统一为3位，不够的前面补0
        temp = "%02d"% int(r)
        oldname = os.path.join(rootDir, dir)  # 老文件夹的名字
        newname = os.path.join(rootDir, temp)  # 新文件夹的名字
        os.rename(oldname, newname)
        r += 1

if __name__ == '__main__':
    rootdir = r'F:\pycharm_代码\tianchi\result'
    replaceDirName(rootdir)
