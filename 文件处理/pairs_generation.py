from glob import glob
import numpy as np
import random
import argparse
import os
class pairs():
    def __init__(self, imagesPath, noOfPositiveExamples, noOfNegativeExamples, imgExtension="JPEG"):
        self.imagesPath = imagesPath  # 目录的路径，其中是带有图像的文件夹（每个文件夹 - 不同的类别）path of a directory where are folders with images (each folder - different category)
        self.noOfPositiveExamples = noOfPositiveExamples  #每个目录中正数（“相同”）示例数 number of positive ("same") examples per category
        self.noOfNegativeExamples = noOfNegativeExamples  #每个目录中负数（“不同”）示例数 number of negative ("different") examples per category
        self.imgExtension = imgExtension  #image扩展格式（.jpg，.JPEG等） image extension format (.jpg, .JPEG etc)
    
    def get_all_images_in_lists(self):
        self.images = []#获得每类下各图片的绝对路径
        folderList = glob(self.imagesPath + '*/')#用它可以查找符合特定规则的文件路径名
        for folder_i, folder in enumerate(folderList):
            imgPathList = glob(folder + '*' + self.imgExtension)#索引到每类文件下的找寻jpeg图片的路径
            self.images.append(imgPathList)
        self.noOfCategories = len(self.images)#不同类文件下的图片个数
    
    def get_random_two_images(self, listA, listB):
        imageA = np.random.choice(listA)
        imageB = np.random.choice(listB)
        #np.random.choice(eq) 随机从eq中选取
        # make sure they are not the same image: 确保它们不是同一个图像
        while (imageA == imageB):
            imageB = np.random.choice(listB)
        return "/".join(imageA.split("/")[-2:]), "/".join(imageB.split("/")[-2:])
    
    def create_pairs(self):
        # returns 2D list of the format "[pathToImageA, pathToImageB, label]"  返回格式为“[图片A路径，图片B路径，标签]”的2D列表
        pairsList = []  # empty list for all the information  所有信息的空列表
        # iterate through all the categories in the dataset:  遍历数据集中的所有类别：
        for i in range(self.noOfCategories):
            print("Class", i + 1, "out of", self.noOfCategories)
            negativeCategoriesList = np.delete(np.arange(0, self.noOfCategories), i)
            # get "noOfPositiveExamples" of pairs with label "1": 得到与标有“1”对“noOfPositiveExamples”：
            for k in range(self.noOfPositiveExamples):
                #u= np.random.choice(negativeCategoriesList)
                #imageA, imageB = self.get_random_two_images(self.images[i], self.images[i])
                imageA, imageB = self.get_random_two_images(self.images[i], self.images[i])
                pairsList.append([imageA, imageB, "1"])
            # get "noOfNegativeExamples" of pairs with label "0":  获取标签为“0”对“noOfNegativeExamples”：
            for k in range(self.noOfNegativeExamples):
                j = np.random.choice(negativeCategoriesList)
                imageA, imageB = self.get_random_two_images(self.images[i], self.images[j])
                pairsList.append([imageA, imageB, "0"])
        return pairsList
    
    def split_list_into_four_textfiles(self, pairsList, txtFilesDir="./txtFiles/"):
        trainFileLeft = ""
        trainFileRight = ""
        valFileLeft = ""
        valFileRight = ""
        random.shuffle(pairsList)  # shuffle list of pairs  打乱随机排序双图片对象的列单
        for line in pairsList:
            # choose randomly if it's a val or train case (split 70/30): 如果是val或火车案例，则随意选择（拆分70/30）
            if (random.random() > 0.3):
                trainFileLeft += line[0] + " " + line[2] + "\n"  # first image path + label 第一图像路径+标签
                trainFileRight += line[1] + " " + line[2] + "\n"  # second image path + label
            else:
                valFileLeft += line[0] + " " + line[2] + "\n"  # first image path + label
                valFileRight += line[1] + " " + line[2] + "\n"  # second image path + label
        
        # Save all four files: 保存所有四个文件
        if (not os.path.exists(txtFilesDir)):
            os.makedirs(txtFilesDir)  # create the folder if one does not exist 创建文件夹（如果不存在
        f = open(txtFilesDir + "train_left.txt", "w")
        f.write(trainFileLeft)
        f.close()
        f = open(txtFilesDir + "train_right.txt", "w")
        f.write(trainFileRight)
        f.close()
        f = open(txtFilesDir + "val_left.txt", "w")
        f.write(valFileLeft)
        f.close()
        f = open(txtFilesDir + "val_right.txt", "w")
        f.write(valFileRight)
        f.close()


# ------------------------------------------------------------------

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir',
        type=str,
        default=r"F:\网络数据集\lfw\测试\tra\0",
        help="Directory where are stored images (folders of images)"#“存储图像的目录（图像文件夹）”
    )
    parser.add_argument(
        '--examples',
        type=int,
        default=100,
        help="Number of positive examples per category"#“每个类别的正面例子数量”
    )
    parser.add_argument(
        '--txt_dir',
        type=str,
        default="./txtFiles/",
        help="Directory where text files will be saved"#“将保存文本文件的目录”
    )
    FLAGS = parser.parse_args()
    
    #tra_01 = r"F:\网络数据集\lfw\测试\tra\0"  # 存放匹配对象
    
    trainingPairsGenerator = pairs(FLAGS.dir, FLAGS.examples, FLAGS.examples)
    
    trainingPairsGenerator.get_all_images_in_lists()
    pairsList = trainingPairsGenerator.create_pairs()
    trainingPairsGenerator.split_list_into_four_textfiles(pairsList, FLAGS.txt_dir)