"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 09排列组合的迭代.py
@Desc    : 09排列组合的迭代
@Software: PyCharm
"""
from itertools import permutations

items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)


# 得到指定长度的排列
for p in permutations(items, 2):
    print(p)

