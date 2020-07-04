#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.runoob.com/python3/python3-tuple.html
# Python3 元组 | 菜鸟教程
# demo tuple 序列 元组
# 我对元组的理解：元组即元素的组合，其他语言一般称之为数组

# 实例
# Java的写法 new String[]{"a", "b"}
# js 的写法 ["a", "b", 1, 2]
tup1 = ('Java', 'Javascript', 'Python', 'PHP')
tup2 = (2010, 2016, 2019, 2020, 2022)
tup3 = 'a', 'b', 'c', 'd', 6, 9

# 打印类型
print(tup1)
print(tup2)
print(tup3)

# 空元组
# Java写法 new String[0];
# js写法 []
tupEmpty = ()

# 一个元素时，需要加逗号
# 不写逗号，首先编辑器报不规范，然后类型检测为元素的类型
tupOne1 = (50)
print("整型：", type(tupOne1))
tupOne2 = (50,)
print("元组：", type(tupOne2))

# 1、访问元组
print("索引访问：", tup1[2])
print("索引区间访问：", tup1[2:3])
# 2、修改元组，元组元素值不可修改，这一点与java和js都不用
# 元组可以组合
print("组合元组：", tup1 + tup2)
# 3、删除元组
# 元素不可删，只能删元组
tupDel = ('d', 'e', 'l', 'e', 't', 'e')
del tupDel
print("元组删除之后不能调用")

# 4、元组运算符
print('len: ', len(tup1))
print('+: ', tup1 + tup2)
print('*: ', ('1',) * 4)
print('in: ', 'a' in tup3)
for x in tup1:
    print(x)

# 5、元组索引，截取
print("索引访问：", tup1[2])
print("负值索引：", tup2[-2])
print("范围索引：", tup3[1:])
# print("索引越界：", tup1[-123])

# 6、元组内置函数
print("len: ", len(tup1))
# max min 不支持不用类型元素的情况
print("max: ", max(tup2))
print("min: ", min(tup2))
print("tuple: ", tuple(['list', 'tuple']))

