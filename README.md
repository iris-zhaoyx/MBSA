<div align="center">

# 1  Install environment
Please follow the instructions in DATASET.md.


# 2  Target Movement Area(TMA)

## 2.1 data preparation
A dataset for identifying personnel including doctors, children, and parents.


## 2.2 Acquisition of Time Intervals of Interest(TIOI)
To obtain the TIOI, we use the real-time speech transcription service provided by iFLYTEK.
We then intercept video clips based on the timestamps and obtain the number of times the assessment occurred.

## 2.3 Acquisition of Spatio-Temporal Regions of Interest (ST-ROI)
Person Identification Model Training
```python
cd /TMA/
python train.py --data data/mydata.yaml --cfg models/yolov5s.yaml --weights 'weights/yolov5s.pt' --batch-size 16
```

detect
```python
cd /TMA/
python detect.py --save-txt --source file_path --weights model.pt_path(s)
```

crop by bounding-box
```python
cd /TMA/
python txt2json.py
python json2csv.py
python size_unify.py
python crop_img.py
python resize.py
```

## 2.4 Acquisition of Spatio-Temporal Regions of Interest (ST-ROI)
```python
cd /TMA/
python img2video.py
```

# 3  Action Recognition

## 3.1 data preparation
A dataset called SS-ASD contains seven categories of actions (turning, pointing, airplane playing, car pushing, toy jumping, water drinking, and watching people).
SS-ASD:https://github.com/iris-zhaoyx/MBSA.

## 3.2 train
```python
cd /Adaptformer/
OMP_NUM_THREADS=1 python3 -m torch.distributed.launch --nproc_per_node=1 --nnodes=1 --node_rank=0 --master_addr=localhost --master_port=2345 --use_env main_video.py --finetune 'models/checkpoints/pretrain_vit_b_1600.pth' --output_dir './output' --batch_size 16 --epochs 1000 --blr 0.01 --weight_decay 0.0 --dist_eval --data_path './data/' --data_set SSV2 --ffn_adapt --nb_classes 7
```

## 3.3 inference
```python
cd /Adaptformer/
OMP_NUM_THREADS=1 python3 -m torch.distributed.launch --nproc_per_node=1 --nnodes=1 --node_rank=0 --master_addr=localhost --master_port=2345 --use_env main_video.py --finetune 'model.pth_path' --output_dir './output' --blr 0.1 --weight_decay 0.0 --eval --dist_eval --data_path './data/' --data_set SSV2 --ffn_adapt
```


# Acknowledgement

The project is based on [VideoMAE](https://github.com/MCG-NJU/VideoMAE), [AdaptFormer](https://github.com/ShoufaChen/AdaptFormer), and [yolov5](https://github.com/HowieMa/DeepSORT_YOLOv5_Pytorch).
Thanks for their awesome works.