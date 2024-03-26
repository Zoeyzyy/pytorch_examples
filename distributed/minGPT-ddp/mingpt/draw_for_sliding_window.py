import multiprocessing
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np

# 创建解析器
parser = argparse.ArgumentParser(description='Process some parameters.')

# 添加参数
parser.add_argument('--accuracy', help='time gap')
parser.add_argument('--from_to', help='from or to')

# 解析命令行参数
args = parser.parse_args()

real_epoch_time_plot = []
sliding_window_epoch_time_plot = []

accuracy = (int)(args.accuracy)
from_to = args.from_to


def time_to_float(time_str):
    hours, minutes, seconds = map(float, time_str.split(':'))
    return hours * 60 * 60 + minutes * 60 + seconds


# 读取step.txt文件中的数字
with open('step.txt', 'r') as file:
    for line in file:
        line = line.split()
        real_epoch_time_plot_i = time_to_float(line[1])
        real_epoch_time_plot.append(real_epoch_time_plot_i)

for i in range(len(real_epoch_time_plot)):
    epoch_time_gap = real_epoch_time_plot[1] - real_epoch_time_plot[0]
    sliding_window_epoch_time_plot.append(
        real_epoch_time_plot[0] + epoch_time_gap * i)

from106 = np.loadtxt('./Sum_by_time/Sum_by_Time_from106_'+ str(accuracy)).tolist()
from108 = np.loadtxt('./Sum_by_time/Sum_by_Time_from108_'+ str(accuracy)).tolist()
from112 = np.loadtxt('./Sum_by_time/Sum_by_Time_from112_'+ str(accuracy)).tolist()

def draw_sliding_window(window_i):
    print("draw sliding window ", window_i)
    x_l = (sliding_window_epoch_time_plot[window_i] -
           sliding_window_epoch_time_plot[0]) * 10 ** (int)(accuracy - 9.0)
    x_r = (sliding_window_epoch_time_plot[window_i + 1] -
           sliding_window_epoch_time_plot[0]) * 10 ** (int)(accuracy - 9.0)
    print(x_l, x_r)
    data = from106[x_l:x_r]
    print(data)
    # x 坐标的间隔
    time_interval = 10 ** (int)(- accuracy + 9.0)
    # x 坐标范围
    x_values = [i * time_interval for i in range(len(data))]

    # 设置子图布局
    fig, axs = plt.subplots(1, 1, figsize=(8, 10))

    # 绘制第一个子图
    axs[0].bar(x_values, data, color='blue')
    axs[0].set_title(str(from_to) + ' 106')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Packet Length Sum (Bytes)')

    # 设置整个图的标题
    fig.suptitle('Packet Length Sum by Time (time gap ' + str(time_interval) +
                 's & window ' + str(window_i + 1) + ' )', fontsize=16)

    # 调整布局
    plt.tight_layout()

    # 展示图像
    plt.savefig("./window_time/"+ str(from_to)+"_" + str(accuracy) + "/"+str(from_to)+"_106_" +
                str(accuracy) + "_window" + str(window_i + 1) + ".png")

    data = from108[x_l:x_r]
    # x 坐标的间隔
    time_interval = 10 ** (int)(- accuracy + 9.0)
    # x 坐标范围
    x_values = [i * time_interval for i in range(len(data))]

    # 设置子图布局
    fig, axs = plt.subplots(1, 1, figsize=(8, 10))

    # 绘制第一个子图
    axs[0].bar(x_values, data, color="blue")
    axs[0].set_title(str(from_to)+' 108')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Packet Length Sum (Bytes)')

    # 设置整个图的标题
    fig.suptitle('Packet Length Sum by Time (time gap ' + str(time_interval) +
                 's & window ' + str(window_i + 1) + ' )', fontsize=16)

    # 调整布局
    plt.tight_layout()

    # 展示图像
    plt.savefig("./window_time/"+ str(from_to)+"_" + str(accuracy) + "/"+str(from_to)+"_108_" +
                str(accuracy) + "_window" + str(window_i + 1) + ".png")

    data = from112[x_l:x_r]
    # x 坐标的间隔
    time_interval = 10 ** (int)(- accuracy + 9.0)
    # x 坐标范围
    x_values = [i * time_interval for i in range(len(data))]

    # 设置子图布局
    fig, axs = plt.subplots(1, 1, figsize=(8, 10))

    # 绘制第一个子图
    axs[0].bar(x_values, data, color="blue")
    axs[0].set_title(str(from_to) + ' 112')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Packet Length Sum (Bytes)')

    # 设置整个图的标题
    fig.suptitle('Packet Length Sum by Time (time gap ' + str(time_interval) +
                 's & window ' + str(window_i + 1) + ' )', fontsize=16)

    # 调整布局
    plt.tight_layout()

    # 展示图像
    plt.savefig("./window_time/"+ str(from_to)+"_" + str(accuracy) + "/"+str(from_to)+"_112_" +
                str(accuracy) + "_window" + str(window_i + 1) + ".png")


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=100)
    for window_i in range(0, 100):
        pool.apply_async(draw_sliding_window, (window_i, ))
    pool.close()
    pool.join()
    print("Sub-process(es) done.")