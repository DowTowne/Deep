#-*=coding:utf-8 -*-
from numpy import *
# arange 等差数列
a = arange(15).reshape(3,5)
a
a.shape       # shape的返回值是一个元组，里面每个数字表示每一维的长度
a.ndim        # 数组的维数
a.ndtype.name # 数组中元素类型的名称
a.itemsize    # 数组中每个元素的字节大小
type(a)       #
