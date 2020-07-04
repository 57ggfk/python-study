#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m
import pickle

# 输入和输出 IO


# 一、格式化输出
# 函数返回一个用户易读的表达形式

print(str('Hello Python'))
print(str('Hello Python\t\b\r\n'))
#  产生一个解释器易读的表达形式
print(repr('Hello Representation'))
print(repr('Hello Representation\n'))
print(repr('Hello Representation\t\r\n'))
# format
print("格式化输出，占位符使用{}".format("{我是占位符}"))
print("格式化输出，占位符位置索引{1}{0}".format("『位置索引0』", "『位置索引1』"))
print("参数名格式化，{name} {age}".format(name='我是name参数', age="我是age参数"))
print("位置及关键字参数 {0} {1} {other}".format("1", "2", other="其他"))

print("数字宽度格式化，{0:2d} {1:3d} {2:5d}".format(12, 2, 3))
print("浮点数{0:.3f}".format(m.pi))

# 引用全局方法 !a ascii() !s str() !r repr()
print("引用ASCII，{!a}".format("a"), "ascii()", ascii('\n'))
print("引用STRING，{!s}".format("str\t\b\r\n"))
print("引用REPRESENT，{!r}".format("repr\t\b\r\n"))

# 0填充，不足位数补0，包括小数；超过位数不处理
print('12'.zfill(5))
print('-3.45'.zfill(7))
print('3.1415926'.zfill(3))

# 模拟文本对齐效果
print("我是左对齐".ljust(20))
print("我是右对齐".rjust(20))
print("我是中心对齐".center(20))

# 传入字典格式化
table = {'key1': 1, 'key2': 2}
print("传入字典格式化，{0[key1]} {0[key2]}".format(table))
print("传入字典格式化，{key1} {key2}".format(**table))
print("传入字典格式化，{key1:d} {key2:d}".format(**table))
print("传入字典格式化，{key1:2d} {key2:2d}".format(**table))

# 传统的字符串格式化
print("传统的字符串格式化，%s" % '「我是字符串」')
print("传统的字符串格式化，%i" % 1)
print("传统的字符串格式化，%f" % 1.2)
print("传统的字符串格式化，%d" % 12)
print("传统的字符串格式化，多个参数：%d %i %f %s" % (12, 1, 1.1, 'str'))

# 新式格式化
format_param1 = "参数1"
format_param2 = "参数2"
print(f'新式格式化 {format_param1} {format_param2}')
print(f'新式格式化 {12} {32}')
print(f'新式格式化 {"参数1"} {"参数2"}')

# 二、读取键盘输入
# inp = input("请输入：")
# print("你输入了：", inp)

# 三、读写文件


def read_file(file_path):
    """
    读文件
    :param file_path: 文件路径
    :return: 无
    """
    fr = open(file_path, 'r')
    print(fr.readlines())
    fr.close()


def write_file(file_path, context):
    """
    以覆盖方式写文件
    :param file_path: 文件路径
    :param context: 内容
    :return: 无
    """
    fw = open('files/write.txt', 'w')
    fw.write(context)
    fw.close()


def append_file(file_path, context):
    """
    以追加方式写文件
    :param file_path: 文件路径
    :param context: 内容
    :return: 无
    """
    a = open(file_path, 'a')
    a.writelines(context)
    a.close()


# 读文件
f = open('files/read.txt', 'r')
print(f.read())
f.close()

# 写文件
write_file('files/write.txt', "# This file is for writing.\n")
read_file('files/write.txt')
# 以追加方式写文件
append_file('files/write.txt', "# This file is for appending.")
read_file('files/write.txt')

# 清除内容
write_file('files/write.txt', "")
read_file('files/write.txt')

# 四、序列化模块 pickle
obj = {'key1': 1, 'key2': 2}
wb = open("files/obj.ser", "wb")
# 序列化
pickle.dump(obj, wb)
wb.close()

# 反序列化
wb = open("files/obj.ser", "rb")
load_obj = pickle.load(wb)
wb.close()
print(load_obj)

