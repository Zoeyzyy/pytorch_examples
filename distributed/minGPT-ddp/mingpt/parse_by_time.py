from datetime import datetime

pcap_name = "../../../1.pcap"
epochfile_name = "step.txt"

# 读取文件
with open(epochfile_name, 'r') as epochfile:
    lines = epochfile.readlines()

epoch_times = {}

line_num = 0
for line in lines:
    parts = line.split()
    epoch_times[parts[1]] = line_num
    line_num += 1

# 读取文件
with open(pcap_name, 'r') as file:
    lines = file.readlines()

# 创建一个字典来存储每个时间点的累加数字
time_sums = {}

def find_max_key_less_than_x(dictionary, x):
    max_key = None
    for key in dictionary.keys():
        if key < x:
            if max_key is None or key > max_key:
                max_key = key
    return max_key

# 遍历每一行
for line in lines:
    # 检查是否包含[P.]，并提取时间和数字
    if '[P.]' in line and 'length' in line:
        parts = line.split()
        time_str = parts[0]  # 时间字符串
        time_str = time_str[:10]
        length_index = parts.index('length')  # 查找 'length' 的位置
        x_index = length_index + 1  # 数字的位置在 'length' 之后
        if x_index < len(parts):
            x = float(parts[x_index])
            if x != 0:
                # 将数字累加到对应时间点
                time_sums[time_str] = time_sums.get(time_str, 0) + x

# 画图
import matplotlib.pyplot as plt

# 提取时间和累加值
times = []
sums = []
i = 0
for time_key, sum_value in time_sums.items():
    times.append(float(time_key[6:14]))
    sums.append(sum_value)
print(times[0])
print(len(times))
print(len(sums))

def adjust_list(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            # 当前数值比前一个数值小
            for j in range(i, len(lst)):
                lst[j] += 60
    first_element = lst[0]
    return [x - first_element for x in lst]

times = adjust_list(times)

# 绘制柱状图
plt.bar(times, sums, color='skyblue')
plt.xticks(times[::100])

# 添加标题和标签
plt.title('Packet length Sum by Time')
plt.xlabel('Time(s)')
plt.ylabel('Packet length Sum(Bytes)')

# 自动调整布局
plt.tight_layout()

# 保存图像
plt.savefig('sum_by_time.png')

