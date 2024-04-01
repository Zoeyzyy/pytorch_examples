import matplotlib.pyplot as plt

epoch_time_plot_3 = []
epoch_time_plot_4 = []
epoch_time_plot_6 = []

epoch_time_gap_3 = []
epoch_time_gap_4 = []
epoch_time_gap_6 = []
epoch_time_gap_all = []

def time_to_float(time_str):
    hours, minutes, seconds = map(float, time_str.split(':'))
    return hours * 60 * 60 + minutes * 60 + seconds

# 读取step length文件中的数字
with open('./step2time_index/step2time_index_3_12', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_3.append(float(line[0]))
    
    for i in range(1, len(epoch_time_plot_3)):
        epoch_time_gap_3.append(epoch_time_plot_3[i] - epoch_time_plot_3[i - 1])

# 绘制直方图
plt.hist(epoch_time_gap_3, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 3)')

# 显示图形
plt.savefig('./epoch_time_distribute/3_distribution.png')
plt.close()

with open('./step2time_index/step2time_index_4_12', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_4.append(float(line[0]))
    
    for i in range(1, len(epoch_time_plot_4)):
        epoch_time_gap_4.append(epoch_time_plot_4[i] - epoch_time_plot_4[i - 1])

# 绘制直方图
plt.hist(epoch_time_gap_4, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 4)')

# 显示图形
plt.savefig('./epoch_time_distribute/4_distribution.png')
plt.close()

with open('./step2time_index/step2time_index_6_12', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_6.append(float(line[0]))
    
    for i in range(1, len(epoch_time_plot_6)):
        epoch_time_gap_6.append(epoch_time_plot_6[i] - epoch_time_plot_6[i - 1])

# 绘制直方图
plt.hist(epoch_time_gap_6, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 6)')

# 显示图形
plt.savefig('./epoch_time_distribute/6_distribution.png')
plt.close()

epoch_time_gap_all = epoch_time_gap_3 + epoch_time_gap_4 + epoch_time_gap_6

# 绘制直方图
plt.hist(epoch_time_gap_all, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine all)')

# 显示图形
plt.savefig('./epoch_time_distribute/all_distribution.png')
plt.close()
