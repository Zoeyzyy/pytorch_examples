import matplotlib.pyplot as plt
import glob
import os
import pickle

epoch_time_plot = []
communication_start_time = []

def time_to_float(time_str):
    hours, minutes, seconds = map(float, time_str.split(':'))
    return hours * 60 * 60 + minutes * 60 + seconds

# 读取step.txt文件中的数字
with open('./master/step.txt', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_i = time_to_float(line[1])
        epoch_time_plot.append(epoch_time_plot_i)

# 初始化communication_start_time列表
communication_start_time = [None] * len(epoch_time_plot)

# 定义文件路径
from_files = os.path.join('../../..', 'from*.txt')
to_files = os.path.join('../../..', 'to*.txt')

# 尝试从文件中加载communication_start_time
if os.path.exists('./communication_start_distribute/communication_start_time_108.pkl'):
    with open('./communication_start_distribute/communication_start_time_108.pkl', 'rb') as f:
        communication_start_time = pickle.load(f)
else:
    # 遍历from*.txt文件
    for file in glob.glob(from_files):
        with open(file, 'r') as f:
            print(file)
            for line in f:
                parts = line.split()  # 假设每行的时间和其他数据之间用空格分隔
                current_time = float(time_to_float(parts[0]))
                # 遍历epoch时间
                for i in range(len(epoch_time_plot)):
                    if current_time >= epoch_time_plot[i]:
                        if communication_start_time[i] is None or current_time - epoch_time_plot[i] < communication_start_time[i]:
                            communication_start_time[i] = current_time - epoch_time_plot[i]
                    else:
                        break

    # 遍历to*.txt文件
    for file in glob.glob(to_files):
        with open(file, 'r') as f:
            print(file)
            for line in f:
                parts = line.split()  # 假设每行的时间和其他数据之间用空格分隔
                current_time = float(time_to_float(parts[0]))
                # 遍历epoch时间
                for i in range(len(epoch_time_plot)):
                    if current_time >= epoch_time_plot[i]:
                        if communication_start_time[i] is None or current_time - epoch_time_plot[i] < communication_start_time[i]:
                            communication_start_time[i] = current_time - epoch_time_plot[i]
                    else:
                        break
    
    # 将communication_start_time保存到文件中
    with open('./communication_start_distribute/communication_start_time_108.pkl', 'wb') as f:
        pickle.dump(communication_start_time, f)


# 绘制直方图
plt.hist(communication_start_time, bins=30, color='skyblue', edgecolor='black')

# 添加标签和标题
plt.xlabel('Start Time of Communication(s)')
plt.ylabel('Frequency')
plt.title('Distribution of start time of communication (Machine 108)')

# 显示图形
plt.savefig('./communication_start_distribute/108_distribution.png')
