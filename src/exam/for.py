#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

# 打印单行文本

print("打印单行文本: ")
for x in range(0, 10):
    print(x, end=' ')
print()
for x in range(0, 10):
    print('*', end=' ')
print()

# 打印多行文本
print("打印多行文本: ")
for x in range(0, 5):
    for y in range(0, 10):
        print('*', end=' ')
    print()

# 取模
print("取模方式1：")
for x in range(0, 20):
    if x != 0 and x % 5 == 0:
        # 换行
        print()
    print('*', end=' ')

print("取模方式2：")
for x in range(0, 20):
    print('*', end=' ')
    if x % 5 == 4:
        # 换行
        print()

print("取模查看值：")
for x in range(0, 20):
    print(x % 5, end=' ')
    if x % 5 == 4:
        # 换行
        print()

print("打印ascii: ")
for x in range(0, 127):
    print(chr(x), end='\t')
    if x % 16 == 16 - 1:
        print()
print()

print("打印ascii对照表：")
for x in range(0, 127):
    print(str(x) + ': ', end='')
    print(chr(x), end='\t')
    if x % 16 == 16 - 1:
        print()
print()

print("打印4种三角形：")
angle = 0
for x in range(0, 5):
    angle = angle + 1
    for y in range(0, angle):
        print('*', end=' ')
    print()
# angle = 5
for x in range(0, 5):
    angle = angle - 1
    for y in range(0, angle):
        print('*', end=' ')
    print()
# angle = 0
for x in range(0, 5):
    angle = angle + 1
    for y in range(1, angle):
        print(' ', end=' ')
    for z in range(0, 5 - x):
        print('*', end=' ')
    print()
# angle = 5
for x in range(0, 5):
    angle = angle - 1
    for y in range(0, angle):
        print(' ', end=' ')
    for z in range(0, 5 - angle):
        print('*', end=' ')
    print()

#
print("打印正三角形: ")
for x in range(0, 10):
    for y in range(x, 10 - 1):
        print('', end=' ')
    for z in range(0, x + 1):
        print('*', end=' ')
    print()

print("打印菱形：")
lenRhombus = 12
for x in range(0, lenRhombus):
    if x < lenRhombus // 2:
        for y in range(x, lenRhombus // 2 - 1):
            print('', end=' ')
        for z in range(0, x + 1):
            print('*', end=' ')
        print()
    elif x > lenRhombus // 2:
        for y in range(lenRhombus // 2, x):
            print('', end=' ')
        for z in range(x, lenRhombus):
            print('*', end=' ')
        print()


