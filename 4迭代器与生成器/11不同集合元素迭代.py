"""
# coding:utf-8
@Time    : 2021/06/15
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 11不同集合元素迭代.py
@Desc    : 11不同集合元素迭代
@Software: PyCharm
"""
"""
很多时候我们需要在不同的集合上进行相同的操作，常见的方法如下
"""
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
salt = 'test'

for i in a:
    print(f'a[i]+salt is {str(i) + salt}')

for j in b:
    print(f'b[j]+salt is {str(j) + salt}')

from itertools import chain

for x in chain(a, b):
    print(f'{x}+salt is {str(x) + salt}, with function chain.')

# chain函数接收一个或多个可迭代对象作为输入，然后创建一个迭代器，按照参数输入顺序一次返回可迭代对象中的每个元素


