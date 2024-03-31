local_ip = 3

all_ip = [3, 4, 6]

with open("TM.txt", "w") as file:
    pass

# 打开文件以写入模式
with open("sh_parse.sh", "w") as file:
    file.write("rm ./*.png \n")
    for ip in all_ip:
        # 向文件中写入内容
        if(ip != local_ip):
            file.write("tcpdump -r ./packet/from" + str(ip) +".pcap > ./packet/from" + str(ip) +".txt \n")
            file.write("tcpdump -r ./packet/to" + str(ip) +".pcap > ./packet/to" + str(ip) +".txt \n")
            file.write("python3 parse.py  --sender=" + str(ip) + " --reciever=" + str(local_ip) + " --pcap_file from" + str(ip) +" & \n")
            file.write("python3 parse.py  --sender=" + str(local_ip) + " --reciever=" + str(ip) + " --pcap_file to" + str(ip) +" & \n")

import subprocess

# 调用shell命令运行.sh文件
subprocess.run(["sh", "sh_parse.sh"])

accuracys = [8, 10, 11, 12] # 1s, 0.1s, 0.01s, 0.001s

# 打开文件以写入模式
with open("sh_parse_by_time.sh", "w") as file:
    for accuracy in accuracys:
        for ip in all_ip:
            # 向文件中写入内容
            if(ip != local_ip):
                file.write("python3 parse_by_time.py --sender=" + str(ip) + " --reciever=" + str(local_ip) + " --accuracy=" + str(accuracy) +" --pcap_file from" + str(ip) +" & \n")
                file.write("python3 parse_by_time.py --sender=" + str(local_ip) + " --reciever=" + str(ip) + " --accuracy=" + str(accuracy) +" --pcap_file to" + str(ip) +" & \n")

import subprocess

# 调用shell命令运行.sh文件
subprocess.run(["sh", "sh_parse_by_time.sh"])



