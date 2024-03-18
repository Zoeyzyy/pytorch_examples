from datetime import datetime
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description='Process some parameters.')

# 添加参数
parser.add_argument('--pcap_file', help='pcap file name')
parser.add_argument('--sender')
parser.add_argument('--reciever')

# 解析命令行参数
args = parser.parse_args()

pcap_name = "../../../"+ args.pcap_file +".txt"
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

import re

def is_valid_time(time_str):
    pattern = r'^\d{2}:\d{2}:\d{2}\.\d+$'
    return bool(re.match(pattern, time_str))

# 遍历每一行
for line in lines:
    # 检查是否包含[P.]，并提取时间和数字
    if '[P.]' in line and 'length' in line:
        parts = line.split()
        time_str = parts[0]  # 时间字符串
        if is_valid_time(parts[0]):
            length_index = parts.index('length')  # 查找 'length' 的位置
            x_index = length_index + 1  # 数字的位置在 'length' 之后
            if x_index < len(parts):
                if not parts[x_index].isdigit():
                    parts[x_index] = parts[x_index][:-1]
                try:
                    x = float(parts[x_index])
                    if x != 0:
                        # 将数字累加到对应时间点
                        max_key = find_max_key_less_than_x(epoch_times, time_str)
                        if max_key is not None:
                            epoch_time = epoch_times[max_key]
                            time_sums[epoch_time] = time_sums.get(epoch_time, 0) + x
                except ValueError:
                    print(line)

# 画图
import matplotlib.pyplot as plt

# 提取时间和累加值
times = []
sums = []
for time_key, sum_value in time_sums.items():
    times.append(time_key)  # 转换时间格式为字符串
    sums.append(sum_value)
print(times)
print(sums)

# 绘制柱状图
plt.bar(times, sums, color='skyblue')

# 添加标题和标签
plt.title('Packet length Sum by Epoch ('+ args.reciever + 'reciever, ' + args.sender +' sender )')
plt.xlabel('Epoch')
plt.ylabel('Packet length Sum')

# 自动调整布局
plt.tight_layout()

# 保存图像
plt.savefig('sum_by_epoch_'+ args.pcap_file + '.png')

