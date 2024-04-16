'''
generate_sum_by_time.py:
目的： 生成Sum_by_Time的数据0.01 0.001 0.0001粒度，以主节点对齐时间

方法：
1. 主函数：不同粒度, !! 修改node = 4

'''
import concurrent.futures
from util import get_files_by_suffix, read_th_line, count_lines, time_to_float, remove_last_char_if_not_digit, create_file

packet_path = "./packet"
step_path = "./master"

def generate_sum_by_time(time_step, node):
    filenames = get_files_by_suffix(packet_path, ".txt")
    filenames = [filename for filename in filenames if "step" not in filename]
    
    master_step_line_number = count_lines( step_path + "/step_master.txt")
    start_time = read_th_line( step_path + "/step_master.txt", 0)
    start_time = start_time.split()[1]
    end_time = read_th_line( step_path + "/step_master.txt", master_step_line_number - 1)
    end_time = end_time.split()[1]
    print(start_time, end_time)
    
    float_time_step = time_step.replace('_', '.')
    len_sum_by_time = (int)((time_to_float(end_time) - time_to_float(start_time)) / (float)(float_time_step)) + 1
    
    for filename in filenames:
        sum_by_time = [0] * len_sum_by_time
        # 打开文件
        with open(packet_path + "/" + filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "seq" in line:
                    line = line.split()
                    current_time = time_to_float(line[0])
                    time_index = (int)((current_time - time_to_float(start_time)) / (float)(float_time_step))
                    # 寻找"length" 的index
                    length_index = line.index("length")
                    if time_index >= 0 and time_index < len_sum_by_time:
                        sum_by_time[time_index] += remove_last_char_if_not_digit(line[length_index + 1])

            
            # 存储到文件中
            from_to = filename.split(".")[0]
            storename = "/Sum_by_Time/Sum_by_time_node" + str(node) + "_" + from_to + "_" + time_step
            create_file(storename)
            # sum_by_time记录到storefile中，每一行一个数据
            with open(storename, 'w') as f:
                for i in sum_by_time:
                    f.write(str(i) + '\n')   
                

# 主函数
if __name__ == '__main__':
    time_steps = ["1_0", "0_1","0_01", "0_001"] # , "0_0001"
    node = 4
    # 使用 ThreadPoolExecutor 创建一个线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 使用 map 方法并行执行 draw 函数
        executor.map(generate_sum_by_time, time_steps, [node]*len(time_steps))