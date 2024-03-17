python -m torch.distributed.launch \
--master_addr=172.22.5.106 --master_port=22346 \
--nproc_per_node=1 --nnodes=2 --node_rank=0 \
multigpu_torchrun.py 5 1 