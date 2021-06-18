"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 10遍历多个序列.py
@Desc    : 10遍历多个序列
@Software: PyCharm
"""
from itertools import zip_longest
a = [1, 2, 3, 5]
b = [6, 7, 8, 9, 10, 11, 12, 13]

# zip默认遍历输出较短的序列
for x in zip(a, b):
    print(x)

# 通过zip_longest输出最长的
for x in zip_longest(a, b):
    print(x)

# 通过指定fillvalue参数来指定长度不够的序列输出
for x in zip_longest(a, b, fillvalue=0):
    print(x)
