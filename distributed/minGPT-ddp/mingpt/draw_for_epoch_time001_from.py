import matplotlib.pyplot as plt
import numpy as np

from106_0_001 = np.loadtxt('./Sum_by_time/Sum_by_Time_from106_0.001').tolist()
from108_0_001 = np.loadtxt('./Sum_by_time/Sum_by_Time_from108_0.001').tolist()
from112_0_001 = np.loadtxt('./Sum_by_time/Sum_by_Time_from112_0.001').tolist()

step106 = np.loadtxt('./step2time_index/step2time_index_106_12').tolist()
step108 = np.loadtxt('./step2time_index/step2time_index_108_12').tolist()
step112 = np.loadtxt('./step2time_index/step2time_index_112_12').tolist()

def first_nonzero_index(lst):
    for i, num in enumerate(lst):
        if num != 0:
            return i
    return len(lst)

def min_nonzero_index(lst1, lst2, lst3):
    min_index = min(first_nonzero_index(lst1), first_nonzero_index(lst2), first_nonzero_index(lst3))
    return min_index


def last_nonzero_index(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] != 0:
            return i
    return -1

def max_nonzero_index(lst1, lst2, lst3):
    max_index = max(last_nonzero_index(lst1), last_nonzero_index(lst2), last_nonzero_index(lst3))
    return max_index

position_l = min(step106[0], step108[0], step112[0])
position_r = max_nonzero_index(from106_0_001, from108_0_001, from112_0_001)

step106 = [x - position_l for x in step106]
step108 = [x - position_l for x in step108]
step112 = [x - position_l for x in step112]

zeros = [0] * (int(step106[0]))
from106_0_001 = zeros + from106_0_001
zeros = [0] * (int(step108[0]))
from108_0_001 = zeros + from108_0_001
zeros = [0] * (int(step112[0]))
from112_0_001 = zeros + from112_0_001

label = ["from 106","from 108","from 112"]

colors = ['blue', 'orange', 'green', 'red']

def draw(epoch_i):
    if epoch_i == 9:
        x_l = min(step106[epoch_i], step108[epoch_i], step112[epoch_i])
        x_r = position_r
    else:
        x_l = min(step106[epoch_i], step108[epoch_i], step112[epoch_i])
        x_r = max(step106[epoch_i + 1], step108[epoch_i + 1], step112[epoch_i + 1])
    if epoch_i != 9:
        data1 = ([0] * (int(step106[epoch_i]) - int(x_l))) + (from106_0_001[int(step106[epoch_i]): int(step106[epoch_i + 1])]) + ([0] * (int(x_r) - int(step106[epoch_i + 1])))
        data2 = ([0] * (int(step108[epoch_i]) - int(x_l))) + (from108_0_001[int(step108[epoch_i]): int(step108[epoch_i + 1])]) + ([0] * (int(x_r) - int(step108[epoch_i + 1])))
        data3 = ([0] * (int(step112[epoch_i]) - int(x_l))) + (from112_0_001[int(step112[epoch_i]): int(step112[epoch_i + 1])]) + ([0] * (int(x_r) - int(step112[epoch_i + 1])))
    else:
        data1 = ([0] * (int(step106[epoch_i]) - int(x_l))) + (from106_0_001[int(step106[epoch_i]): int(x_l + 20000)])
        data2 = ([0] * (int(step108[epoch_i]) - int(x_l))) + (from108_0_001[int(step108[epoch_i]): int(x_l + 20000)])
        data3 = ([0] * (int(step112[epoch_i]) - int(x_l))) + (from112_0_001[int(step112[epoch_i]): int(x_l + 20000)])

    print(epoch_i, len(data1), len(data2), len(data3))
    assert len(data1) == len(data2) and len(data3) == len(data2), "data 1 2 3 不长度相等"
    
    # x 坐标的间隔
    time_interval = 0.001
    # x 坐标范围
    x_length = len(data1)
    x_values = [i * time_interval for i in range(len(data1))]

    # 设置子图布局
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))

    # 绘制第一个子图
    axs[0].bar(range(len(data1)), data1, color = colors[0])
    axs[0].set_title('from 106')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Packet Length Sum (Bytes)')

    # 绘制第二个子图
    axs[1].bar(range(len(data2)), data2, color = colors[1])
    axs[1].set_title('from 108')
    axs[1].set_xlabel('Time (ms)')
    axs[1].set_ylabel('Packet Length Sum (Bytes)')

    # 绘制第三个子图
    axs[2].bar(range(len(data3)), data3, color = colors[2])
    axs[2].set_title('from 112')
    axs[2].set_xlabel('Time (ms)')
    axs[2].set_ylabel('Packet Length Sum (Bytes)')


    # 设置整个图的标题
    fig.suptitle('Packet Length Sum by Time (time gap 0.001s & epoch ' + str(epoch_i + 1) + ' )', fontsize=16)

    # 调整布局
    plt.tight_layout()

    # 展示图像
    plt.savefig("./epoch_time/from0_001s/from0_001s_epoch" + str(epoch_i + 1) + ".png")

import multiprocessing
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=10)
    for epoch_i in range(0, 10):
        pool.apply_async(draw, (epoch_i, ))
    pool.close()
    pool.join()
    print("Sub-process(es) done.")
