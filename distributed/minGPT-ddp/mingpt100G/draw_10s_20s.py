'''
目的: 画0.01 0.001 0.0001粒度下的在10s-20s时序图
方法：
1. 每一个节点获得Sum_by_Time_node3_to6_0_01的数据
3. 从10s的index开始,到20s的index结束, 每张图的数据取自Sum_by_Time_node2_from6的相同index的数据

generate_sum_by_time.py:
1. 生成Sum_by_Time的数据0.01 0.001 0.0001粒度，以主节点对齐时间

'''

from util import count_lines, get_files_by_suffix, read_th_line, create_file
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl

packet_path = "./"
step_path = "./master"

def draw_time_serie(time_line, float_time_step, start_index, name):
    #设置全局字体大小
    mpl.rcParams['font.size'] = 16
    
    x = [x * float_time_step for x in range(start_index, start_index + len(time_line))]
    y = [(int)(y) for y in time_line]
    
    plt.figure()
    # 绘制矩阵图
    bar_width = 1.0 / len(time_line)
    plt.plot(x, y, color='skyblue')
    
    # 添加坐标轴含义
    plt.xlabel('Time(s)')
    plt.ylabel('Communication(Bytes)')
    create_file( packet_path + "/time_series/"+ str(time_step) +"/10s_20s" + str(name) + "_" + str(time_step) + ".png")
    plt.savefig( packet_path + "/time_series/"+ str(time_step) +"/10s_20s" + str(name) + "_" + str(time_step) + ".png")
    plt.close()
    
# 计算时序图的index，画出index_count范围内的时序图
def draw_time_series(time_step, index_count):
    float_time_step = float(time_step.replace('_', '.'))
    start_index = (int)(10 / float_time_step) # 10s开始的10s的时序图
    # 获得./Sum_by_time下的每一个以time_step结尾的文件名
    names = ["node3_from3", "node3_from4", "node3_from6",
             "node4_from3", "node4_from4", "node4_from6",
             "node6_from3", "node6_from4", "node6_from6",
             "node3_to3", "node3_to4", "node3_to6",
             "node4_to3", "node4_to4", "node4_to6",
             "node6_to3", "node6_to4", "node6_to6"]
    filenames = [ packet_path + "/Sum_by_Time/Sum_by_time_" + name + f"_{time_step}" for name in names]  
    
    for i in range(len(filenames)):
        filename = filenames[i]
        name = names[i]
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                time_line = lines[start_index: (int)(start_index + index_count + 1)]
                draw_time_serie(time_line, float_time_step, start_index, name)
                
        

# 主函数
if __name__ == '__main__':
    time_steps = ["1_0", "0_1","0_01", "0_001"]
    float_time_steps = [1.0, 0.1, 0.01, 0.001]
    index_count = [(20 - 10) / x for x in float_time_steps]
    for time_step, index_count in zip(time_steps, index_count):
        draw_time_series(time_step, index_count)
        
