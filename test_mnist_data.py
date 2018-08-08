# -*- coding: utf-8 -*-

import tensorflow as tf

# 导入input_data用于自动下载和安装MNIST数据集
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print( mnist.train.next_batch(1))
