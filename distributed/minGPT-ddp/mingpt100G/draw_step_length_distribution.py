import matplotlib.pyplot as plt

epoch_time_plot_3 = []
epoch_time_plot_4 = []
epoch_time_plot_6 = []

epoch_time_gap_3 = []
epoch_time_gap_4 = []
epoch_time_gap_6 = []

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
plt.figure(figsize=(10, 10))
plt.hist(epoch_time_gap_3, bins=30, color='skyblue', edgecolor='black')

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
plt.figure(figsize=(10, 10))
plt.hist(epoch_time_gap_4, bins=30, color='skyblue', edgecolor='black')

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
plt.figure(figsize=(10, 10))
plt.hist(epoch_time_gap_6, bins=30, color='skyblue', edgecolor='black')

# 添加标签和标题
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')
plt.title('Distribution graph of epoch time (Machine 6)')

# 显示图形
plt.savefig('./epoch_time_distribute/6_distribution.png')
plt.close()


# 汇总至一张图
data1 = epoch_time_gap_3
data2 = epoch_time_gap_4
data3 = epoch_time_gap_6

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
plt.title('Distribution graph of epoch time')
plt.xlabel('Epoch time(s)')
plt.ylabel('Frequency')

# 添加图例
plt.legend()

# 显示图形
plt.savefig('./epoch_time_distribute/all_distribute.png')