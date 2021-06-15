"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 05反向迭代 .py
@Desc    : my_reverse
@Software: PyCharm
"""
"""
可以通过实现__reverse__方法来实现反向迭代
"""


class CountDown(object):
    def __init__(self, start, step=1):
        self.start = start
        self.step = step

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= self.step

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += self.step


for rr in reversed(CountDown(30)):
    print(rr)


for rr in CountDown(30, 2):
    print(rr)
