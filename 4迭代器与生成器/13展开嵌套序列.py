"""
# coding:utf-8
@Time    : 2021/06/15
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 13展开嵌套序列.py
@Desc    : 13展开嵌套序列
@Software: PyCharm
"""
"""
如果你想展开一个嵌套的序列，可以通过yield from来操作
"""
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        # 判断序列是否是Iterable对象同时不属于str bytes类型，通过yield from 代码迭代到父生成器
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

items = [1, 2, ['abc', 'qec', [3, 4], 5], 'hello']
for x in flatten(items):
    print(x)

"""
当你在生成器中想调用其他子生成器作为子例程的时候可以使用yield from，如果不使用yield from的话，则需要多写一层for循环
"""


def flatten_with_from(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for child in flatten_with_from(x):
                yield child
        else:
            yield x


for x in flatten_with_from(items):
    print(x)
