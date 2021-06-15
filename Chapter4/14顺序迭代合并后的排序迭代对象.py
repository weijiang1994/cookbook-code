"""
# coding:utf-8
@Time    : 2021/06/15
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 14顺序迭代合并后的排序迭代对象.py
@Desc    : 14顺序迭代合并后的排序迭代对象
@Software: PyCharm
"""
from heapq import merge

a = [1, 2, 4, 6, 8]
b = [3, 5, 7, 9]

for x in merge(a, b):
    print(x)
