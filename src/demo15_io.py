#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import math as m

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
print("引用STRING，{!s}".format("str\t\b\s\r\n"))
print("引用REPRESENT，{!r}".format("repr\t\b\s\r\n"))

# 0填充，不足位数补0，包括小数；超过位数不处理
print('12'.zfill(5))
print('-3.45'.zfill(7))
print('3.1415926'.zfill(3))

# 模拟文本对齐效果
print("我是左对齐".ljust(20))
print("我是右对齐".rjust(20))
print("我是中心对齐".center(20))

# 传入字典格式化
table = { 'key1': 1, 'key2': 2 }
print("传入字典格式化，{0[key1]} {0[key2]}".format(table))
print("传入字典格式化，{key1} {key2}".format(**table))
print("传入字典格式化，{key1:d} {key2:d}".format(**table))
print("传入字典格式化，{key1:2d} {key2:2d}".format(**table))

# 传统的字符串格式化
print("传统的字符串格式化，%s"%'「我是字符串」')

# 二、读取键盘输入


# 三、读写文件


# 四、序列化模块 pickle
