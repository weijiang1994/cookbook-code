"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 07迭代器切片.py
@Desc    : 07迭代器切片
@Software: PyCharm
"""
from itertools import islice


def count(c):
    while True:
        yield c
        c += 1


# 迭代器生成器不适用标准的切片
try:
    count(0)[10: 20]
except TypeError:
    import traceback
    traceback.print_exc()

# 使用islice函数将迭代器进行切片
for i in islice(count(0), 10, 20):
    print(i)

"""
迭代器与生成器不能使用标准的切片操作，因为一开始不知道其长度切索引未知。
通过islice函数进行切片需要注意的是它会消耗传入迭代器的数据，如果你需要进行切片后再次访问的话，你需要先将其保存到一个列表中。
"""