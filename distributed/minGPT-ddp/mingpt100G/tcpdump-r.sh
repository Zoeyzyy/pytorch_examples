#!/bin/bash

# 指定要遍历的目录
base_dir="./"

# 遍历以packet_开头的文件夹
for folder in $base_dir/packet_*; do
    # 检查是否是文件夹
    if [ -d "$folder" ]; then
        # 进入文件夹
        cd "$folder" || continue
        # 遍历以.pcap结尾的文件
        for pcap_file in *.pcap; do
            # 检查是否是文件
            if [ -f "$pcap_file" ]; then
                # 提取文件名（不包含扩展名）
                filename=$(basename -- "$pcap_file" .pcap)
                # 检查是否已经存在同名的.txt文件
                if [ ! -e "$filename.txt" ]; then
                    # 运行tcpdump命令并将结果保存为同名的.txt文件
                    tcpdump -r "$pcap_file" > "./$filename.txt"
                fi
            fi
        done
        # 返回上一级目录
        cd ..
    fi
done
