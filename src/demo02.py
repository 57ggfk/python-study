#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import math
import random

'''
Number
在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。与nodejs相同
'''

# 数字类型转换

print(int('1'))
print(float('1.1'))
print(complex('1'))
print(complex(1,2))

# 不同形式的数字
print("普通整数：", 10)
print("普通浮点数：", 0.0)
print("普通复数：", 3.14j)
print("十六进制：", 0xA0F)
print("八进制：", 0o37)
print("科学计数法：", 70.2E-12)

## 数字比较
x, y = 3, 4
print((x > y) - (x < y))

## 数字运算
print("加法：", 2 + 2)
print("减法", 2 - 1)
print("乘法：", 2 * 3)
print("除法，除不尽情况：", 4 / 3)
print("除法，能除尽情况：", 4 / 2)
print("浮点数计算：", 0.1 + 0.2)
print("除法，整数相除向下取整：", 7 // 4)
print("除法，浮点相除向下取整：", 7.1 // 4.2)
print("取余，整数相除取余：", 17 // 3)
print("取余：浮点相除取余", 17 // 3.2)
print("幂运算：", 2 ** 3)
print("整数、浮点数混合运算：", 1 - 1 + 0.1 + 0.2)

# 数学函数
print("绝对值：", abs(-1))
print("绝对值：", math.fabs(-1))
print("平方根：", math.sqrt(2))
print("立方根：", math.pow(2, 3))
print("e的次幂：", math.exp(2))
print("对数log：", math.log(math.e))
print("对数log10：", math.log10(100))
print("向上取整：", math.ceil(1.1))
print("向下取整：", math.floor(2.8))
print("四舍五入：", round(1.235, 2))
print("最大值：", min(1, 2))
print("最小值：", max(2, 3))

# 随机数
print("随机挑选：", random.choice(range(10)))
print("范围挑选：", random.randrange(0, 5, 1))
print("随机数[0,1]：", random.random())
# print("种子随机：", random.seed())
print("随机排序：", random.shuffle([1, 2, 3]))
print("随机实数：", random.uniform(1, 10))

# 三角函数 略

# 数学常量
print("PI: ", math.pi)
print("E: ", math.e)





