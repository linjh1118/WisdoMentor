# 下载llama-factory，执行以下命令
# 全参预训练
CUDA_VISIBLE_DEVICES=2,3,4,5,6,7 /home/work/linjinghao01/llama_factory/bin/python -m torch.distributed.launch --nnodes=1 --nproc-per-node=6 --master_port=7786 --use-env src/train_bash.py  \
    --deepspeed deepspeed.json \
    --stage pt \
    --model_name_or_path /home/work/linjinghao01/weight/baichuan-chat \
    --do_train \
	--dataset train_title_v1_pt \
    --template baichuan2 \
    --finetuning_type full \
    --output_dir output/train_title_v1_pt \
    --overwrite_cache \
    --per_device_train_batch_size 8 \
    --gradient_accumulation_steps 1 \
    --preprocessing_num_workers 8 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 500 \
    --learning_rate 5e-5 \
    --max_grad_norm 0.5 \
    --num_train_epochs 3.0 \
    --plot_loss \
    --fp16


# 全参sft
CUDA_VISIBLE_DEVICES=0,1,2,3 /ssd3/linjinghao01/llama_factory/bin/python -m torch.distributed.launch --nnodes=1 --nproc-per-node=4 --master_port=7788 --use-env src/train_bash.py  \
    --deepspeed deepspeed.json \
    --stage sft \
    --model_name_or_path /home/work/linjinghao01/weight/baichuan-chat \
    --do_train \
    --dataset summary_wx_train_v2 \
    --template baichuan2 \
    --finetuning_type full \
    --output_dir output/sft/summary_wx_train_v2 \
    --overwrite_cache \
    --per_device_train_batch_size 16 \
    --gradient_accumulation_steps 4 \
    --preprocessing_num_workers 4 \
    --lr_scheduler_type constant \
	--adam_beta1 0.9 \
	--adam_beta2 0.98 \
	--adam_epsilon 1e-8 \
	--weight_decay 1e-4 \
    --logging_steps 1 \
	--warmup_ratio 0.0 \
    --save_steps 1000 \
    --learning_rate 1e-5 \
    --max_grad_norm 1.0 \
    --num_train_epochs 2.0 \
	--gradient_checkpointing True \
	--plot_loss \
    --fp16

# 全参dpo
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 /deepspeed --num_gpus=5 src/train_bash.py \
CUDA_VISIBLE_DEVICES=1 /home/work/linjinghao01/llama_factory/bin/python -m torch.distributed.launch --nnodes=1 --nproc-per-node=1 --master_port=7788 --use-env src/train_bash.py  \
    --deepspeed deepspeed.json \
    --stage sft \
    --model_name_or_path /home/work/linjinghao01/weight/baichuan-chat \
    --do_train \
    --dataset summary_wx_train_v2 \
    --template baichuan2 \
    --finetuning_type lora \
	--lora_target W_pack \
    --output_dir output/sft/summary_wx_train_v2_lora \
    --overwrite_cache \
    --per_device_train_batch_size 16 \
    --gradient_accumulation_steps 8 \
    --preprocessing_num_workers 4 \
    --lr_scheduler_type constant \
	--adam_beta1 0.9 \
	--adam_beta2 0.98 \
	--adam_epsilon 1e-8 \
	--weight_decay 1e-4 \
    --logging_steps 1 \
	--warmup_ratio 0.0 \
    --save_steps 1000 \
    --learning_rate 1e-5 \
    --max_grad_norm 1.0 \
    --num_train_epochs 2.0 \
	--gradient_checkpointing True \
	--plot_loss \
    --fp16

