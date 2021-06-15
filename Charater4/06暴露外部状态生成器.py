"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 06暴露外部状态生成器.py
@Desc    : 如果你想暴露一些生成器函数属性给外部调用者，可以通过生成器类来实现
@Software: PyCharm
"""

from collections import deque


class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('somefile.txt') as f:
    lh = LineHistory(f)
    for line in lh:
        if 'python' in line:
            for lineno, hline in lh.history:
                print(f'{lineno}:{hline}')
