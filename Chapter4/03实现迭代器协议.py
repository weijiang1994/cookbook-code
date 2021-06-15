"""
目前为止，在一个对象上实现迭代最最简单的方式是使用一个生成器函数，在4.2小节中，
使用Node类来表示树型数据结构。
那可能想实现一个以深度优先方式便利树型节点的生成器。
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        # 最开始返回本身
        yield self
        # 因为实现了iter方法通过for进行迭代
        for c in self:
            # 返回子节点depth_first
            yield from c.depth_first()
        # 实现深度优先遍历


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
