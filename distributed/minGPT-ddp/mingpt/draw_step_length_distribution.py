import matplotlib.pyplot as plt

epoch_time_plot_106 = []
epoch_time_plot_108 = []
epoch_time_plot_112 = []

epoch_time_gap_106 = []
epoch_time_gap_108 = []
epoch_time_gap_112 = []
epoch_time_gap_all = []

def time_to_float(time_str):
    hours, minutes, seconds = map(float, time_str.split(':'))
    return hours * 60 * 60 + minutes * 60 + seconds

# 读取step length文件中的数字
with open('./step2time_index/step2time_index_106_12', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_106.append(float(line[0]))
    
    for i in range(1, len(epoch_time_plot_106)):
        epoch_time_gap_106.append(epoch_time_plot_106[i] - epoch_time_plot_106[i - 1])

# 绘制直方图
plt.hist(epoch_time_gap_106, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 106)')

# 显示图形
plt.savefig('./epoch_time_distribute/106_distribution.png')
plt.close()

with open('./step2time_index/step2time_index_108_12', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_108.append(float(line[0]))
    
    for i in range(1, len(epoch_time_plot_108)):
        epoch_time_gap_108.append(epoch_time_plot_108[i] - epoch_time_plot_108[i - 1])

# 绘制直方图
plt.hist(epoch_time_gap_108, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 108)')

# 显示图形
plt.savefig('./epoch_time_distribute/108_distribution.png')
plt.close()

with open('./step2time_index/step2time_index_112_12', 'r') as file:
    for line in file:
        line = line.split()
        epoch_time_plot_112.append(float(line[0]))
    
    for i in range(1, len(epoch_time_plot_112)):
        epoch_time_gap_112.append(epoch_time_plot_112[i] - epoch_time_plot_112[i - 1])

# 绘制直方图
plt.hist(epoch_time_gap_112, bins=30, color='skyblue', edgecolor='black')
plt.figure(figsize=(1000, 80))

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 112)')

# 显示图形
plt.savefig('./epoch_time_distribute/112_distribution.png')
plt.close()

epoch_time_gap_all = epoch_time_gap_106 + epoch_time_gap_108 + epoch_time_gap_112

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
