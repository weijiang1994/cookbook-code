"""
# coding:utf-8
@Time    : 2021/06/16
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 01读写文件.py
@Desc    : 01读写文件
@Software: PyCharm
"""
# 最简单的读取方式，其中rt可以省略，因为默认就是该模式
with open('sample.txt', 'rt') as f:
    print(f.read())

print('='*70)

# 与上面的效果一样
with open('sample.txt') as f:
    print(f.read())

