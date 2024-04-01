import matplotlib.pyplot as plt
from datetime import datetime
import argparse
import os
import numpy as np
import re

# 创建解析器
parser = argparse.ArgumentParser(description='Process some parameters.')

# 添加参数
parser.add_argument('--accuracy', help='time gap')
parser.add_argument('--from_to', help='from or to')
parser.add_argument('--sender')
parser.add_argument('--reciever')
parser.add_argument('--epoch_num', help='epoch numbers')

# 解析命令行参数
args = parser.parse_args()
accuracy = (int)(args.accuracy)

def find_files_with_pattern(folder_path, pattern):
    # 初始化匹配结果列表
    matching_files = []

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否匹配模式
            if re.match(pattern, file):
                # 如果匹配，将文件的完整路径添加到匹配结果列表中
                matching_files.append(os.path.join(root, file))

    return matching_files

def time_to_float(time_str):
    hours, minutes, seconds = map(float, time_str.split(':'))
    return hours * 60 * 60 + minutes * 60 + seconds

def find_max_key_less_than_x(dictionary, x):
    max_key = None
    for key in dictionary.keys():
        if key < x:
            if max_key is None or key > max_key:
                max_key = key
    return max_key

def is_valid_time(time_str):
    pattern = r'^\d{2}:\d{2}:\d{2}\.\d+$'
    return bool(re.match(pattern, time_str))

# # 定义要搜索的文件夹路径
# folder_path = "./packet/"

# # 定义要匹配的文件名模式
# if args.from_to == "from":
#     pattern = r"from.*\.txt"
# elif args.from_to == "to":
#     pattern = r"to.*\.txt"

# # 查找匹配的文件
# pcap_names = find_files_with_pattern(folder_path, pattern)

# epochfile_name = "step.txt"

# # 读取文件
# with open(epochfile_name, 'r') as epochfile:
#     lines = epochfile.readlines()

# epoch_times = {}

# line_num = 0
# for line in lines:
#     parts = line.split()
#     epoch_times[parts[1]] = line_num
#     line_num += 1

# # 创建一个字典来存储每个时间点的累加数字
# time_sums = {}

# for pcap_name in pcap_names:
#     # 读取文件
#     with open(pcap_name, 'r') as file:
#         lines = file.readlines()

#     # 遍历每一行
#     for line in lines:
#         # 检查是否包含[P.]，并提取时间和数字
#         if 'length' in line:
#             parts = line.split()
#             if is_valid_time(parts[0]):
#                 time_str = parts[0]  # 时间字符串
#                 time_str = time_str[:accuracy]
#                 x_index = len(parts) - 1
#                 try:
#                     while(len(parts[x_index]) > 0 and not parts[x_index].isdigit()):
#                         parts[x_index] = parts[x_index][:-1]
#                     x = float(parts[x_index])
#                     if x != 0:
#                         # 将数字累加到对应时间点
#                         time_sums[time_str] = time_sums.get(time_str, 0) + x
#                 except ValueError:
#                     print(line)
#                     print("!")
#             else:
#                 print(parts[0])
#                 pass

# step2time_index = []
# with open('step.txt', 'r') as stepfile:
#     lines = stepfile.readlines()
#     for line in lines:
#         line = line.split()
#         step_time = time_to_float(line[1][:accuracy])
#         step2time_index.append(step_time)     

# # 提取时间和累加值
# times = []
# sums = []
# i = 0
# for time_key, sum_value in time_sums.items():
#     times.append(time_to_float(time_key[:accuracy])) # 秒为单位
#     sums.append(sum_value)

# print(len(times))
# print(len(sums))

# len_new_times = (int)((max(times) - step2time_index[0]) * 10 ** (accuracy - 9.0) + 1)
# # 初始化 times 和 sums 列表
# new_times = [i * 10 ** (- accuracy + 9.0) for i in range(len_new_times)]  # 10 ** -(accuracy - 9.0)秒为单位
# new_sums = [0] * len_new_times

# print(len(new_times))
# print(len(new_sums))
# print(min(times), max(times), step2time_index[0])

# # 将已有的数据填充到新的列表中
# for i, time in enumerate(times):
#     # 找到对应的索引，由于时间单位为 0.001 秒，因此乘以 1000 转换为整数索引
#     index = (int)((time - step2time_index[0]) * 10 ** (accuracy - 9.0))
#     if index < len(new_sums) and index >= 0:
#         new_sums[index] = sums[i]
#     else:
#         # print("!!", index, sums[i])
#         # print("!!", ((time - step2time_index[0]) * 10 ** (accuracy - 9.0)))
#         pass

# times = new_times
# sums = new_sums   

# 将列表Sum_by_time和step2time_index写入文本文件
# if args.from_to == "from":
#     np.savetxt('./Sum_by_time/Sum_by_Time_from108_' + str(10 ** -(accuracy - 9.0)) , sums)
# else:
#     np.savetxt('./Sum_by_time/Sum_by_Time_to108_' + str(10 ** -(accuracy - 9.0)), sums)

# np.savetxt('./step2time_index/step2time_index_108_' + str(accuracy), step2time_index)

print("savetxt")

if args.from_to == "from":
    new_sums = np.loadtxt('./Sum_by_time/Sum_by_Time_from108_' + str(10 ** -(accuracy - 9.0))).tolist()
else:
    new_sums = np.loadtxt('./Sum_by_time/Sum_by_Time_to108_' + str(10 ** -(accuracy - 9.0))).tolist()
new_times = [i * 10 ** (- accuracy + 9.0) for i in range(len(new_sums))]  # 10 ** -(accuracy - 9.0)秒为单位
step2time_index = np.loadtxt('./step2time_index/step2time_index_108_' + str(accuracy)).tolist()
print(len(new_times))

# 绘制 sum_by_time_all 图像
# 绘制柱状图
if hasattr(args, 'epoch_num') and args.epoch_num is not None:
    epoch_num = (int)(args.epoch_num)
    print("epoch_num: ", epoch_num)
    x_sum_by_time_all = new_times[: (int)((step2time_index[epoch_num] - step2time_index[0]) * 10 ** (accuracy - 9.0))]
    y_sum_by_time_all = new_sums[: (int)((step2time_index[epoch_num] - step2time_index[0]) * 10 ** (accuracy - 9.0))]
    print("len_sum_by_time_all: ", len(x_sum_by_time_all), len(y_sum_by_time_all))
    plt.figure(figsize=(40, 6), dpi=1200)
    plt.bar(x_sum_by_time_all, y_sum_by_time_all, color='skyblue', width=(float)(40.0 / len(x_sum_by_time_all)))
    
    # 添加标题和标签
    if accuracy == 8:
        if args.from_to == "from":
            plt.title('Packet length Sum by Time ( from 108 and ' + str(10 ** -(accuracy - 8.0)) + 's )')
        else:
            plt.title('Packet length Sum by Time ( to 108 and ' + str(10 ** -(accuracy - 8.0)) + 's )')
    else:
        if args.from_to == "from":
            plt.title('Packet length Sum by Time ( from 108 and ' + str(10 ** -(accuracy - 9.0)) + 's )')
        else:
            plt.title('Packet length Sum by Time ( to 108 and ' + str(10 ** -(accuracy - 9.0)) + 's )')
    plt.xlabel('Time(s)')
    plt.ylabel('Packet length Sum(Byte)')

    # 保存图像
    if accuracy == 8:
        plt.savefig('./by_time/sum_by_time_'+ str(10 ** -(accuracy - 8.0)) + 's_' + args.from_to + 'all108.png')
    else:
        plt.savefig('./by_time/sum_by_time_'+ str(10 ** -(accuracy - 9.0)) + 's_' + args.from_to + 'all108.png')