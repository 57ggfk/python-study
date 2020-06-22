#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 模块 module 模块导入 与 包管理

# 一、import 导入语句

# 导入内建Built-in模块，标准模块
import sys

print(sys)

# 导入自定义模块
from src.module import support

support.print_func('import')

# 导入多个模块
from src.module import support1, support2

support1.print_func("导入多个模块1")
support2.print_func("导入多个模块2")

# 部分导入，导入模块的部分名称到当前命名空间
from src.module.double_module import print_func1, print_func2

print_func1("多个导入01")
print_func2("多个导入02")

from src.module.multi_module import *

print_multi_01("全部导入01")
print_multi_02("全部导入02")
print_multi_03("全部导入03")

# 模块独立运行代码 __name__ == '__main__'
from src.module import stand
stand.do_none()

# dir()获取模块所有名称
print(dir(stand))
print(dir(sys))
print(dir())

# 特殊模块sys
# print(sys.ps1)
# print(sys.ps2)

# 二、包管理
# __init__.py
import src.module.pkg1.hello1
# 必须使用全名访问
src.module.pkg1.hello1.do_none()

from src.module.pkg1 import hello2
# 可以直接访问
hello2.do_none()

from src.module.pkg1.hello2 import do_none
# 可以导入模块内名称
do_none()

# 导入内所有模块
# __init__.py内__all__ = ["module1", "module2"]
from src.module.pkg2 import *
hi1.do_none()
hi2.do_none()

# 相对导入，相对包路径导入，包之间导入可用
# 相当于文件系统的相对路径 .代表当前包 ..代表上一层包 ..package 上一层下的package包
from src.module.pkg3 import rela
rela.do_none()

# 导入时制定别名 as
from src.module.pkg2 import hi2 as do_hi2
do_hi2.do_none()