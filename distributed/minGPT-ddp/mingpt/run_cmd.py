local_ip = 108

all_ip = [106, 108, 112]
# all_ip = [106, 112]

# 打开文件以写入模式
with open("cmd.sh", "w") as file:
    file.write("sudo rm ./packet/*.pcap \n")
    for ip in all_ip:
        # 向文件中写入内容
        if(ip != local_ip):
            file.write("sudo nohup tcpdump host 172.22.5." + str(ip) + " -s 128  -w ./packet/from" + str(ip) +".pcap & \n")
            file.write("sudo nohup tcpdump dst 172.22.5." + str(ip) + " -s 128  -w ./packet/to" + str(ip) +".pcap & \n")
    
    file.write("\n")  
    file.write("nohup torchrun --master_addr=172.22.5.106 --master_port=22349 --nproc_per_node=1 --nnodes=" + str(len(all_ip)) +" --node_rank="+ str(all_ip.index(local_ip)) +" main.py & \n")  
        

import subprocess

# 调用shell命令运行.sh文件
subprocess.run(["sh", "cmd.sh"])