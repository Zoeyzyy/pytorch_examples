import re
import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

def read_th_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) > line_number:
            return lines[line_number]
        else:
            return "文件行数不足" + str(line_number) + "行"

def get_files_by_suffix(directory, suffix):
    files = os.listdir(directory)
    return [file for file in files if file.endswith(suffix)]

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

def remove_last_char_if_not_digit(string):
    if string.isdigit():
        return int(string)
    else:
        return int(string[:-1])

def create_file(file_path):
    # 获取文件所在的文件夹路径
    folder_path = os.path.dirname(file_path)

    # 如果文件夹不存在，则递归创建文件夹
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 创建文件，如果文件已存在则不做任何操作
    with open(file_path, 'a'):
        pass