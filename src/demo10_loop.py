#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 循环语句

# while 循环
a = 1
while a < 10:
    print(a, end=', ')
    a = a + 1
print()

# while 循环使用else语句
b = 1
while b < 10:
    print(b, end=', ')
    b = b + 1
else:
    print(b)

# for 语法
list1 = [1, 2, 3, 4, 5, 6]
for one in list1:
    print(one, end=', ')
else:
    print(7)

# range() 函数 包含头不包含尾，默认0开始
# 默认0开始，包含0不包含尾
for i in range(5):
    print(i, end=' ')
print()
# 起始、结束 包含头不包含尾
for i in range(1, 6):
    print(i, end=' ')
print()

# 起始、结束、步长
for i in range(1, 10, 3):
    print(i, end=' ')
print()

# 负数
for i in range(-1, -10, -2):
    print(i, end=' ')
print()

# 结合len()
list2 = [1, 2, 3, 4, 5, 6]
for i in range(len(list2)):
    print(i, end=' ')
print()
# 用range创建list
print(list(range(5)))

# break
for i in range(5):
    print(i, end=' ')
    if i == 3:
        break
print()

for i in range(5):
    for j in range(5):
        print(str(i) + '-' + str(j), end=' ')
        if j == 3:
            # break 跳出与它最近的循环
            break
    print()

# continue

for i in range(5):
    if i == 3:
        continue
    print(i, end=' ')
print()

for i in range(5):
    for j in range(5):
        if j == 3:
            # continue 从与它最近的循环继续
            continue
        print(str(i) + '-' + str(j), end=' ')
    print()

# pass Do nothing
for x in (range(2)):
    pass
