#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from collections import deque

# 数据结构
# 容器数据类型 列表 元组 字典 集合
# 序列包含：字符串、列表、元组、集合
# 常见数据结构：序列 堆栈 队列
# 衍生结构：向量 矩阵

# 1、列表当堆栈使用 后进先出是堆栈

stack = [3, 4, 5]
print("弹出最后一个", stack.pop())
stack.append(6)
print("弹出最近添加的", stack.pop())
stack.append(7)
print(stack)

# 2、列表当队列使用 先进先出是队列
# from collections import deque # 导入双端队列
queue = deque([1, 2, 3, 4, 5])
queue.append(6)
print("弹出第一个", queue.popleft())
queue.appendleft(0)
print("弹出最后一个", queue.popleft())
print(queue)

# 3、推导式，支持列表、集合、字典
# 列表推导式 [结果表达式 循环控制 条件判断]
list1 = [2, 4, 6]
list2 = [3*x for x in list1]
print(list1)

list3 = [3*x for x in list1 if x > 3]
print(list3)

# 集合推导式
set1 = set('123456')
set2 = {x for x in set1 if x not in '456'}
print(set2)

# 字典推导式
dict1 = {x: x**2 for x in (2, 4, 6) if x > 2}
print(dict1)

dict2 = {x: dict1[x] for x in dict1 if x < 6}
print(dict2)

# 4、嵌套列表，矩阵，java中有多维数组
list4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print(list4)

# 5、遍历技巧
# 字典键值对项目遍历
print("字典键值对项目变量:", end=' ')
for k, v in {'a': 1, 'b': 2}.items():
    print(k, v, sep=':', end=', ')
print()

# 列表索引值列举
print("列表索引值列举:", end=' ')
for i, v in enumerate(['a', 'b', 'c']):
    print(i, v, sep=':', end=', ')
print()

# 多序列组合遍历
print("多序列组合遍历:", end=' ')
for a, b in zip(['a', 'b'], (1, 2, 3)):
    print(a, b, sep=':', end=', ')
print()

# 返回排序后的序列
print("列表排序还是列表：", sorted([2, 3, 1]))
print("元组排序变成列表：", sorted((2, 3, 1)))
print("集合排序变成列表：", sorted({2, 3, 1}))

