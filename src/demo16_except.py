#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 错误和异常

# 语法错误
# with True print("无法错误")

# 常见异常
# dbz = 2 / 0 # 除0异常
# 4 + spam * 3 # 变量未定义，触发异常
# plus = '2' + 2 字符与数字相加，触发异常

# 异常处理
# try except
try:
    x = int('a')
except ValueError as err:
    print("不是数字", err)

# 处理多个异常
except (RuntimeError, TypeError, NameError):
    pass

try:
    x = int('b')
    i = 2 / 0
except ValueError:
    print("不是数字")
except ZeroDivisionError:
    print("除数不能为0")

try:
    x = int('b')
    i = 2 / 0
except (ValueError, ZeroDivisionError):
    print("触发异常了")

# try except else
try:
    x = int('1')
    xyz = (1, 3)[3]
except ValueError:
    print("不是数字")
except IndexError:
    print("索引越界异常")
else:
    print("没有触发异常")

# try finally
try:
    [0, 1][2]
except IndexError as err:
    print("异常", err)
else:
    print("没有异常")
finally:
    print("不管有没有异常都执行finally")

# 抛出异常 raise
try:
    raise NameError("抛出异常")
except NameError as err:
    print("异常了", err)

try:
    raise NameError("抛出异常")
except NameError as err:
    print("异常了", err)
    # raise # 处理异常后又抛出异常


# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError("我是自定义异常")
except MyError as e:
    print("打印自定义异常", e.value)

# 清理行为
# 清理语句放到finally中

# with 语句自动关闭文件的例子，基本出现异常了也能保证文件被关系
with open("files/read.txt") as f:
    for line in f:
        print(line)


# 断言
# assert True  # 条件为True 时正常执行
# assert False # 条件为False时触发异常
assert True

assert 1 == 1

# 等价于
# if not expression:
#    raise AssertionError


try:
    assert False, "断言失败"
except AssertionError as ass:
    print(ass)

