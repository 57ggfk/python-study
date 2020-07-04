#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 命名空间与作用域 namespace

# 三种命名空间及顺序 作用范围从大到小，优先顺序则相反
# 内置名称 built-in names
# 全局名称 global names
# 局部名称 local names

# 生命周期取决于作用域

# 示例

var1 = 5  # 全局名称


def some_func():
    var2 = 6  # 局部名称

    def some_inner_func():
        # var1 = 7  # 同的名称可以存着多个命名空间
        # var2 = 7  # 但是规范不建议这么写
        var3 = 7  # 内嵌的局部名称


# 作用域，四种作用域：
# L Local 局部，函数内部
# E Enclosing 既non-local也non-global 内部函数访问外部函数的内部变量，俗称闭包
# G Global 全局
# B Built-in 内建

# 实例
var5 = 5  # 全局


def func1():
    # var6 = var5  # 如果有global声明，在前面也不可以直接访问var5
    global var5  # global声明这是全局变量 可用于修改变量
    var5 = 6     # 修改global声明过的全局变量
    var6 = 6  # func1的局部变量
    print("global声明后可以修改全局变量：", var5)

    def func2():
        print("不加global可以直接访问全局变量：", var5)  # 不加global声明可以访问但不能修改
        nonlocal var6  # nonlocal声明闭包变量 func1的局部变量
        var6 = 16  # 访问nonlocal声明过的闭包变量 func1的局部变量
        var7 = 7  # func2的局部变量
        print("var5: ", var5)
        print("var6: ", var6)
        print("var7: ", var7)

    func2()


func1()

# 内建
import builtins
print(dir(builtins))

