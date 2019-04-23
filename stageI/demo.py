
import sys
sys.path.append('/mnt/g/DeepLearning/text2img/StackGAN-master')
from misc.datasets import TextDataset


import prettytensor as pt
import tensorflow as tf
from misc.custom_ops import leaky_rectify

ef_dim = 128

def generate_condition(c_var):
    pt.flatten()
    conditions =\
        (pt.wrap(c_var).
            flatten().
            custom_fully_connected(ef_dim * 2).
            apply(leaky_rectify, leakiness=0.2))
    mean = conditions[:, :ef_dim]
    log_sigma = conditions[:, ef_dim:]
    return [mean, log_sigma]



print generate_condition([])