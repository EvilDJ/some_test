import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(0, 200)]
def read_txt(txt):
    data = []
    with open(txt,'r') as f:
        for i in f:
            data.append(float(i))
    data = data[0:200]
    return data

los = read_txt('./loss_data_v')
los_jun = read_txt('./loss_data_v_jun')
los_yu = read_txt('./loss_data_v_yu')
los_yu_jun = read_txt('./loss_data_v_jun_yu')
los_s = read_txt('./loss_data_v_s')

# plt.plot(x,los,'-',c = 'black',label= 'No pretreatment')
plt.plot(x,los_yu,'-',c = 'blue',label='NR Pretreatment')
# plt.plot(x,los_jun,'-',c = 'red',label='DF')
plt.plot(x,los_yu_jun,'-',c = 'green',label='NTn Model')
plt.xlabel('Iteration')
plt.ylabel('Loss value')
plt.legend(loc=1)
plt.show()