'''
目的: 画0.01 0.001 0.0001粒度下的在10%处 100 or 1000的流量矩阵图
方法：
1. 一个节点汇集所有的Sum_by_Time_node3_from6_0_01或Sum_by_Time_node3_to6_0_01的数据
2. 依次生成100 or 1000张流量矩阵图
3. 从10%的index开始, 每张图的数据取自Sum_by_Time_node2_from6的相同index的数据

generate_sum_by_time.py:
1. 生成Sum_by_Time的数据0.01 0.001 0.0001粒度，以主节点对齐时间

'''

from util import count_lines, get_files_by_suffix, read_th_line, create_file
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def draw_TM_picture(TM_data, index, time_step, norm):
    # 画矩阵
    matrix = np.array(TM_data).reshape(3, 3)
    
    plt.figure()
    # 绘制矩阵图
    plt.imshow(matrix, cmap='Blues', norm=norm)  # 使用 Blues 颜色映射，数值越大颜色越深
    plt.colorbar()  # 添加颜色条
    
    # 添加坐标轴标签
    plt.xticks([0, 1, 2], [3, 4, 6])
    plt.yticks([0, 1, 2], [3, 4, 6])
    
    # 添加坐标轴含义
    plt.xlabel('sender')
    plt.ylabel('reciever')
    create_file("./TM/"+ str(time_step) +"/TM_index" + str(index) + "_" + str(time_step) + ".png")
    plt.savefig("./TM/"+ str(time_step) +"/TM_index" + str(index) + "_" + str(time_step) + ".png")
    plt.close()
    
# 计算TM的index，画TM_count个矩阵
def draw_TMs(time_step, TM_count):
    start_index = (int)(0.1 * count_lines(f"./Sum_by_Time/Sum_by_time_node3_from6_{time_step}"))
    # 获得./Sum_by_time下的每一个以time_step结尾的文件名
    names = ["node3_from3", "node3_from4", "node3_from6", "node4_from3", "node4_from4", "node4_from6", "node6_from3", "node6_from4", "node6_from6",]
    filenames = ["./Sum_by_Time/Sum_by_time_" + name + f"_{time_step}" for name in names]  
    
    datas = []
    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
            datas.append(lines[start_index: start_index + TM_count + 1])
        else:
            datas.append([])
    
    # 使用 Normalize() 函数设置颜色映射
    vmin = 0
    vmax = 0
    for row in datas:
        row_int = [int(x) for x in row]
        if len(row_int) > 0:
            vmax = max(vmax, max(row_int))
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    
    for i in range(TM_count):
        index = i
        TM_data = []
        # 遍历filenames，如果文件存在
        for data in datas:
            if index < len(data):
                # 读取第index行的数据
                TM_data.append(int(data[index]))
            else:
                TM_data.append(0)
        draw_TM_picture(TM_data, i, time_step, norm)
                
        

# 主函数
if __name__ == '__main__':
    time_steps = ["0_01", "0_001", "0_0001"]
    TM_count = [100, 100, 1000]
    for time_step, TM_count in zip(time_steps, TM_count):
        draw_TMs(time_step, TM_count)
        
