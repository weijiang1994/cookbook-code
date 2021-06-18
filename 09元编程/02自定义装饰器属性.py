"""
# coding:utf-8
@Time    : 2021/06/16
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 02自定义装饰器属性.py
@Desc    : 02自定义属性
@Software: PyCharm
"""
import logging
from functools import wraps, partial


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorator(func):
        logname = name if name else func.__module__
        logmsg = message if message else func.__name__
        log = logging.getLogger(logname)

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal logmsg
            logmsg = new_message

        return wrapper

    return decorator


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'examples')
def spam():
    print('Spam')


logging.basicConfig(level=logging.DEBUG)
add(1, 2)
spam()
add.set_message('I am add function.')
add.set_level(logging.WARNING)
add(2, 3)
