rm gpt_snapshot.pt

sudo tcpdump host 172.22.5.112 > ../../../from112.pcap &
sudo tcpdump host 172.22.5.108 > ../../../from108.pcap &
sudo tcpdump dst 172.22.5.112 > ../../../to112.pcap &
sudo tcpdump dst 172.22.5.108 > ../../../to108.pcap &
torchrun \
--master_addr=172.22.5.106 --master_port=22349 \
--nproc_per_node=1 --nnodes=3 --node_rank=0 \
main.py