import matplotlib.pyplot as plt

epoch_time_plot = []
epoch_time_gap = []

def time_to_float(time_str):
    hours, minutes, seconds = map(float, time_str.split(':'))
    return hours * 60 * 60 + minutes * 60 + seconds

# 读取step.txt文件中的数字
with open('step.txt', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_i = time_to_float(line[1])
        epoch_time_plot.append(epoch_time_plot_i)

for i in range(1, len(epoch_time_plot)):
    epoch_time_gap_i = epoch_time_plot[i] - epoch_time_plot[i - 1]
    epoch_time_gap.append(epoch_time_gap_i)

# 绘制直方图
plt.hist(epoch_time_gap, bins=30, color='skyblue', edgecolor='black')

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 106)')

# 显示图形
plt.savefig('./epoch_time_distribute/106_distribution.png')
