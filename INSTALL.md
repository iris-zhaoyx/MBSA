The codebase is mainly built with following libraries:

- Python 3.6 or higher
- [PyTorch](https://pytorch.org/) and [torchvision](https://github.com/pytorch/vision). <br>
  We can successfully reproduce the main results under two settings below:<br>
  Tesla **A100** (40G): CUDA 11.1 + PyTorch 1.8.0 + torchvision 0.9.0<br>
  Tesla **V100** (32G): CUDA 10.1 + PyTorch 1.6.0 + torchvision 0.7.0
- [timm==0.4.8/0.4.12](https://github.com/rwightman/pytorch-image-models)
- [deepspeed==0.5.8](https://github.com/microsoft/DeepSpeed)
  `DS_BUILD_OPS=1 pip install deepspeed`
- [TensorboardX](https://github.com/lanpa/tensorboardX)
- [decord](https://github.com/dmlc/decord)
- [einops](https://github.com/arogozhnikov/einops)
- easydict
- matplotlib>=3.2.2
- numpy>=1.18.5
- opencv-python>=4.1.2
- Pillow
- ffmpeg
- PyYAML>=5.3.1
- scipy>=1.4.1
- torch>=1.7.0
- torchvision>=0.8.1
- tqdm>=4.41.0
- tensorboard>=2.4.1
- seaborn>=0.11.0
- pandas
- thop     # FLOPS computation
- pycocotools>=2.0     # COCO mAP
- requests