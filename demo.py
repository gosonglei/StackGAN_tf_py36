
# from tensorflow.contrib.framework.python.framework import checkpoint_utils
# var_list = checkpoint_utils.list_variables("E:/text2img_py36_win/ckt_logs/flowers/stageI_2019_04_22_19_14_00/model_4000.ckpt")


# for v in var_list:
#     print(v)

import os
from tensorflow.python.client import device_lib
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"
 
if __name__ == "__main__":
    print(device_lib.list_local_devices())