import matplotlib.pyplot as plt
import numpy as np
x = np.zeros(20)
y = np.arange(20)
count = 0
with open(r'G:/mywork/MT-Siam/loss_data', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.replace('\t',' ')
        list = line.split(" ")
        x[count] = list[0]
        count = count + 1
        if count > 19:
            break
        print(list)
fig , xy = plt.subplots()
inx = xy.plot(y,x,label='loss',color='black')
xy.set_xlabel('iteration')
xy.set_ylabel('loss')
labels = ['train loss']
plt.legend(inx, labels, loc=10)
# plt.grid()
plt.show()
# FPR = [1.0, 1.0, 0.13398692810457516, 0.05, 0.0]
# TPR = [1.0, 1.0, 0.8809523809523809, 0.6, 0.0]
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(FPR, TPR,color='black')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Reciver Operating Characteristics')
# plt.show()