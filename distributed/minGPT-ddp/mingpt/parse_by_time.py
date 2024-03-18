from datetime import datetime
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description='Process some parameters.')

# 添加参数
parser.add_argument('--accuracy', help='time gap')
parser.add_argument('--pcap_file', help='pcap file name')
parser.add_argument('--sender')
parser.add_argument('--reciever')

# 解析命令行参数
args = parser.parse_args()


pcap_name = "../../../"+ args.pcap_file +".txt"
epochfile_name = "step.txt"

accuracy = (int)(args.accuracy)

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
    if 'length' in line:
        parts = line.split()
        if is_valid_time(parts[0]):
            time_str = parts[0]  # 时间字符串
            time_str = time_str[:accuracy]
            x_index = len(parts) - 1
            try:
                while(len(parts[x_index]) > 0 and not parts[x_index].isdigit()):
                    parts[x_index] = parts[x_index][:-1]
                x = float(parts[x_index])
                if x != 0:
                    # 将数字累加到对应时间点
                    time_sums[time_str] = time_sums.get(time_str, 0) + x
            except ValueError:
                print(line)
                print("!")
        else:
            print(parts[0])
            pass

# 画图
import matplotlib.pyplot as plt

# 提取时间和累加值
times = []
sums = []
i = 0
for time_key, sum_value in time_sums.items():
    times.append(float(time_key[6:accuracy]))
    sums.append(sum_value)
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

if len(times) > 0:
    times = adjust_list(times)

# 绘制柱状图
plt.bar(times, sums, color='skyblue')
gap_x = max((int)(len(times) / 5), 1)
plt.xticks(times[::gap_x])

# 添加标题和标签
if accuracy == 8:
    plt.title('Packet length Sum by Time ('+ args.reciever + 'reciever, ' + args.sender +' sender and ' + str(10 ** -(accuracy - 8.0)) + 's )')
else:
    plt.title('Packet length Sum by Time ('+ args.reciever + 'reciever, ' + args.sender +' sender and ' + str(10 ** -(accuracy - 9.0)) + 's )')
plt.xlabel('Time(s)')
plt.ylabel('Packet length Sum(Bytes)')

# 自动调整布局
plt.tight_layout()

# 保存图像
if accuracy == 8:
    plt.savefig('sum_by_time_'+ str(10 ** -(accuracy - 8.0)) + 's_' + args.pcap_file + '.png')
else:
    plt.savefig('sum_by_time_'+ str(10 ** -(accuracy - 9.0)) + 's_' + args.pcap_file + '.png')