#!/usr/bin/env python
# _*_ coding:utf-8 _*_
print("Hello World")
print('hello world!')
# this is a comment

# this is a if statement
# 代码组，关键字开始，冒号colon : 结束
if True:
    print("True")
else:
    print("False")
    print("ok")

# code block identified by indent

# one line split to multi line by backslash "\"
total = "a" + \
    "b" + \
  "2"
print(total)

# 单引号和双引号都可以作为字符串符合，与js和shell类似
word = '单引号'
sentence = "双引号"
paragraph = """这是一个段落，
可以由多行组成"""
# 三引号可以指定多行字符串，Python特性，许特殊记忆

# 等待用户输入
# input("\n\n按下enter继续")

# 同一行显示多条语句，与shell语法接近
import sys; x= 'python'; sys.stdout.write(x + '\n')

# 空行也是代码的一部分只是便于阅读无实际作用

# Print 输出，end="" 不换行
print('不换行输出，',end="")
print("换行输出！")

# 全部导入import 部分导入 from...import
import sys
print("+++++全部导入+++++++")
for i in sys.argv:
    print(i)
print("\n Python路径为：", sys.path)

print("========部分导入========")

from sys import argv,path
print("路径为：", path)

# 多个变量赋值
a = b = c = 1
print(a)
# a1,a2 = 2; 这种写法是错误的
# a1; 变量必须赋值
# print(a1);
a,b,c = 1,2,"python"
#print( a + b +c)
'''
js 可以这样
var a = b = c = 1;
var a,b,c = 1,2,3;
var a=1,b=2,c=3;

java 可以这样
int a=1,b=2,c=3;
int a,b=2; //只有b赋值
'''

'''
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
'''

'''
判断类型
type(值), type(1) ==> <class 'int'>
isinstance(值,类型), isinstance(1.1,float) ==> True
区别
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。

js的判断
值 typeof 类型
java的判断
对象.instanceof(类) 
'''
# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

# 删除对象
del a,b,c

# print(a) # NameError: name 'a' is not defined

# 特殊数值运算
print(type(2 / 4)) # / 总是得到浮点数
print(3 // 2)  # 1 整除
print(2 ** 5)  # 32 乘方

# 复数
print(type(3.14j)) # <class 'complex'>

## 字符串
# 转义 \
# 截取 变量[startIndex:lastIndex] # 索引值以 0 为开始值，-1 为从末尾的开始位置。

str = "Python"
print(str[0:0])  # 空
print(str[0:-1]) # Pytho 相当于长度-1
print(str[0:-2]) # Pyth
print(str[2:3])
print(str[0:5]) # Pytho
print(str[0:6]) # Python str长度是6

print(str + "TEST") # PythonTEST 字符串拼接
print(str * 2) # PythonPython 字符串重复2次

