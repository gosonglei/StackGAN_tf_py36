## StackGan tensorflow

[项目原地址](<https://github.com/hanzhanggit/StackGAN>)

### 原项目依赖环境

python 2.7

[TensorFlow 0.12](https://www.tensorflow.org/get_started/os_setup)

### 修改后项目依赖环境

基于win10 gtx-1050ti运行此项目
CUDA v8.0 & cudnn 8.0
Anaconda3
python3.6 tensorflow=1.4.0 tensorflow-gpu=1.4.0



--------

程序目前问题：

stage-II运行出现

`tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[64,128,128,64]`

不知如何解决~