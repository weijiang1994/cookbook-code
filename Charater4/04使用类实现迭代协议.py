"""
# coding:utf-8
@Time    : 2021/06/08
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 04使用类实现迭代协议.py
@Desc    : iterator_class
@Software: PyCharm
"""


class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, child):
        self._children.append(child)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator:

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)
