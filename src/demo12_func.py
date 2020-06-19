#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 函数 function method

# 基本语法


def func_name():
    """
    基本语法
    """
    print("hello")


# 调用
func_name()


def func_print(s):  # 定义函数
    """
    定义函数
    :param s: 传递字符串 形参命名不应该与全局变量名重复
    :return: 无返回
    """
    print(s)


# 调用函数 传递参数
func_print('hello function')

# 调用可变类型与不可变类型
param_list = [1, 2, 3]
param_tuple = (1, 2, 3)


def change_list(param):
    param[0] = 0


change_list(param_list)
print(param_list)


def change_tuple(param):
    param = (4, 5, 6)


change_tuple(param_tuple)
print(param_tuple)


def func_param(param1, param2):
    """
    两个参数的函数，正常按顺序传参，可根据关键字传参
    :param param1: 参数1
    :param param2: 参数2
    :return: 无返回
    """
    print(param1 + " : " + param2)


# 关键字参数
func_param("参数1", "参数2")

func_param(param2="参数2", param1="参数1")


# ## 不定长参数


def func_len(arg1, *args):
    print(arg1)
    print(args[0])
    print(args)


func_len(1, 2, 3, 4, 5)


def func_star(arg1, *, arg2):
    print("*号单独在参数列表出现：", arg1 + arg2)


# 带*号的后面参数必须使用关键字传入
func_star(1, arg2=2)

# ## 匿名函数 lambda表达式，PyCharm提示不建议这么写？

func_lambda = lambda arg1, arg2: arg1 + arg2

print("lambda表达式函数：", func_lambda(1, 2))


# ## return语句 不带return的返回None


def func_return(arg1, arg2):
    return arg1 + arg2


print("带返回值的函数：", func_return(1, 2))


# ## 强制位置参数
# /前面的参数必须是位置形参，*后面必须是关键字形参
# /, 这里提示格式问题，未知？


def func_pos(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f


print("强制位置参数：", func_pos(1, 1, 3, d=4, e=5, f=6))
