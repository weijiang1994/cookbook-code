"""
# coding:utf-8
@Time    : 2021/06/15
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : 12创建数据处理管道.py
@Desc    : 12创建数据处理管道
@Software: PyCharm
"""
import os
import fnmatch
import gzip
import re
import bz2


def find_file(filepat, top):
    # 在文件夹中查找filepat匹配文件
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    # 这段比较难理解其实就是将输入序列拼接成长的行序列，类似于itertools.chain。yield from 是将yield操作代理到父生成器上去
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = find_file('access.log*', '/home/jiangwei/文档/cookbook/04迭代器与生成器/nginx-log')
files = gen_opener(lognames)
lines = gen_concatenate(files)
aim_lines = gen_grep('(?i)python', lines)
for line in aim_lines:
    print(line.replace('\n', ''))

"""
整段代码中，yield做为生产者，for循环作为消费者
"""