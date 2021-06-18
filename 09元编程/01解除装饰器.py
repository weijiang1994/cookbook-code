"""
# coding:utf-8
@Time    : 2021/06/16
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 01解除装饰器.py
@Desc    : 01解除装饰器
@Software: PyCharm
"""
from functools import wraps


def wrap1(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print('I am wrap1')
        return func(*args, **kwargs)

    return decorator


def wrap2(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print('I am wrap2')
        return func(*args, **kwargs)

    return decorator


@wrap1
def test(a, b):
    return a + b


print(test(1, 2))
# 通过__wrapped__可以解除装饰器函数
oig_test = test.__wrapped__
print(oig_test(1, 2))


@wrap1
@wrap2
def test2(a, b):
    return a + b


print(test2(2, 3))
'''
>>> I am wrap1
>>> I am wrap2
>>> 5
'''
oig_test2 = test2.__wrapped__
# python3.3后只能解除最外层装饰器函数
# python3.3前能解除全部装饰器函数
print(oig_test2(2, 3))
'''
>>> I am wrap2
>>> 5
'''
