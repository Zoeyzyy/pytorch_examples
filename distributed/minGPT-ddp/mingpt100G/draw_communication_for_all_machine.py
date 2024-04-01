import matplotlib.pyplot as plt
import numpy as np
import pickle
import os

data1 = []
data2 = []
data3 = []

if os.path.exists('./communication_start_distribute/communication_start_time_3.pkl'):
    with open('./communication_start_distribute/communication_start_time_3.pkl', 'rb') as f:
        data1 = pickle.load(f)

if os.path.exists('./communication_start_distribute/communication_start_time_4.pkl'):
    with open('./communication_start_distribute/communication_start_time_4.pkl', 'rb') as f:
        data2 = pickle.load(f)

if os.path.exists('./communication_start_distribute/communication_start_time_6.pkl'):
    with open('./communication_start_distribute/communication_start_time_6.pkl', 'rb') as f:
        data3 = pickle.load(f)

plt.figure(figsize=(15, 10))
        
# 计算直方图
counts1, bins1, _ = plt.hist(data1, bins=30, color='skyblue', alpha=0.7, density=True)
counts2, bins2, _ = plt.hist(data2, bins=30, color='lightgreen', alpha=0.7, density=True)
counts3, bins3, _ = plt.hist(data3, bins=30, color='salmon', alpha=0.7, density=True)

# 计算中心点
bin_centers1 = 0.5 * (bins1[1:] + bins1[:-1])
bin_centers2 = 0.5 * (bins2[1:] + bins2[:-1])
bin_centers3 = 0.5 * (bins3[1:] + bins3[:-1])

# 绘制折线图
plt.plot(bin_centers1, counts1, color='blue', linestyle='-', label='Machine 3')
plt.plot(bin_centers2, counts2, color='green', linestyle='-', label='Machine 4')
plt.plot(bin_centers3, counts3, color='red', linestyle='-', label='Machine 6')

# 添加标题和标签
plt.title('Distribution of start time of communication for all machines')
plt.xlabel('Start Time of Communication(s)')
plt.ylabel('Frequency')

# 添加图例
plt.legend()

# 显示图形
plt.savefig('./communication_start_distribute/communication_for_all_distribute.png')
