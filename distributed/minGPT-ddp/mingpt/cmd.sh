torchrun \
--master_addr=172.22.5.106 --master_port=22349 \
--nproc_per_node=1 --nnodes=2 --node_rank=0 \
main.py