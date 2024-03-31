rm ../../../*.pcap 
nohup tcpdump host 172.22.5.106 -s 128  -w ../../../from106.pcap & 
nohup tcpdump dst 172.22.5.106 -s 128  -w ../../../to106.pcap & 
nohup tcpdump host 172.22.5.112 -s 128  -w ../../../from112.pcap & 
nohup tcpdump dst 172.22.5.112 -s 128  -w ../../../to112.pcap & 

nohup torchrun --master_addr=172.22.5.106 --master_port=22349 --nproc_per_node=1 --nnodes=3 --node_rank=1 main.py & 
