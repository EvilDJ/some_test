import os
path = 'G:/网络数据集/json/'  # path是你存放json的路径
json_file = os.listdir(path)
for file in json_file:
    os.system("F:/anaconda_3.6/Scripts/labelme_json_to_dataset.exe %s"%(path + file))
