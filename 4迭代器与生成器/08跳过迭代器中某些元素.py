"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 08跳过迭代器中某些元素.py
@Desc    : 08跳过迭代器中某些元素
@Software: PyCharm
"""
from itertools import dropwhile, islice

# dropwhile函数仅仅会跳过最开始部分的值
with open('droptext.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line.replace('\n', ''))


# 如果事先知道迭代器的长度可以使用islice进行忽略
items = ['a', 'b', 'c', 1, 4, 15, 10]


for item in islice(items, 3, None):
    print(item)

"""
3, None 等价 items[3:]
None, 3 等价 items[:3]
"""
