#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 索引访问
var = "Python"
print("var[2]: ", var[2])
print("var[1:3]: ", var[1:3]) # 包含头不能包含尾

# 字符串拼接
var = "Hello World!"
print("已更新字符串：", var[:6] + "Python!")

print("字符串与数字拼接：", var[6:] + str(1))

print('\a\b\e\000\n\v\t\r\f\o12\x0a\other')

print("字符串重复符号*输出两个a: " + " a" * 2)

print("成员运算符in：" + str('a' in 'abc'))

print("not in：" + str('b' not in 'abc'))

print(r"字符串原型raw输出 \n")
print(R"r/R都代表原型输出")

print(R"%"+"格式化输出，%s今年%d岁 "%("张三", 10))
"""
%%	百分号标记 #就是输出一个%
%c	字符及其ASCII码                  char
%s	字符串                           str                  
%d	有符号整数(十进制)                decimal
%u	无符号整数(十进制)                unsign
%o	无符号整数(八进制)                octal
%x	无符号整数(十六进制)                 hexadecimal
%X	无符号整数(十六进制大写字符)         Hexadecimal
%e	浮点数字(科学计数法)                 
%E	浮点数字(科学计数法，用E代替e)
%f	浮点数字(用小数点符号)                float
%g	浮点数字(根据值的大小采用%e或%f)         
%G	浮点数字(类似于%g)
%p	指针(用十六进制打印值的内存地址)        pointer
%n	存储输出字符的数量放进参数列表的下一个变量中  next
"""

