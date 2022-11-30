# 2 GPUs
# Attention, the following batch size is on single GPU, not all GPUs.
python -m torch.distributed.launch --nproc_per_node=8 train.py \
                                                    --cuda \
                                                    -dist \
                                                    -d coco \
                                                    --root ../maskrcnn/data/ \
                                                    -v fcos50 \
#                                                    -lr 1e-4 \
#                                                    -lr_bk 1e-5 \
#                                                    --batch_size 2 \
                                                    --grad_clip_norm 4.0 \
                                                    --num_workers 4 \
                                                    --schedule 2x \
                                                    # --sybn
                                                    # --mosaic
