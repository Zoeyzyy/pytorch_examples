'''
目的: 画0.01 0.001 0.0001粒度下的在10%处 100 or 1000的流量矩阵图
方法：
1. 一个节点汇集所有的Sum_by_Time_node3_from6_0_01或Sum_by_Time_node3_to6_0_01的数据
2. 依次生成100 or 1000张流量矩阵图
3. 从10%的index开始, 每张图的数据取自Sum_by_Time_node2_from6的相同index的数据

generate_sum_by_time.py:
1. 生成Sum_by_Time的数据0.01 0.001 0.0001粒度，以主节点对齐时间

'''
import concurrent.futures
from util import count_lines, get_files_by_suffix, read_th_line

def draw_TM_picture(TM_data, index, time_step):
    # 画矩阵
    matrix = np.array(TM_data).reshape(3, 3)
    
    # 绘制矩阵图
    plt.imshow(matrix, cmap='Blues')  # 使用 Blues 颜色映射，数值越大颜色越深
    plt.colorbar()  # 添加颜色条
    
    # 添加坐标轴标签
    plt.xticks([0, 1, 2], [1, 2, 3])
    plt.yticks([0, 1, 2], [1, 2, 3])
    
    # 添加坐标轴含义
    plt.xlabel('sender')
    plt.ylabel('reciever')
    plt.savefig("TM_index" + str(index) + "_" + str(time_step) + ".png")
    
# 计算TM的index，画TM_count个矩阵
def draw_TMs(time_step, TM_count):
    start_index = 0.1 * count_lines(f"Sum_by_Time_node3_from6_{time_step}")
    # 获得./Sum_by_time下的每一个以time_step结尾的文件名
    names = ["node3_from3", "node3_from4", "node3_from6", "node4_from3", "node4_from4", "node4_from6", "node6_from3", "node6_from4", "node6_from6",]
    filenames = ["./Sum_by_time/Sum_by_Time_" + name + f"_{time_step}" for name in names]  
    
    for i in range(TM_count):
        index = start_index + i
        TM_data = []
        # 遍历filenames，如果文件存在
        for filename in filenames:
            if os.path.exists(filename):
                # 读取第index行的数据
                line = read_th_line(filename, index)
                TM_data.append(int(line))
            else:
                TM_data.append(0)
        draw_TM_picture(TM_data, i, time_step)
                
        

# 主函数
if __name__ == '__main__':
    time_steps = ["0_01", "0_001", "0_0001"]
    TM_count = [100, 100, 1000]
    # 使用 ThreadPoolExecutor 创建一个线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 使用 map 方法并行执行 draw 函数
        executor.map(draw_TM_picture, time_steps, TM_count)
        
