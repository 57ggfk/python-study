#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代器iterator有两个方法iter()、next()

list1 = [1, 2, 3, 4, 5]

it1 = iter(list1)
print(next(it1))
print(next(it1))

# for
for x in iter(list1):
    print(x, end=' ')
print()

# while
it2 = iter(list1)
while True:
    try:
        print(next(it2), end=' ')
    except StopIteration:
        print()
        break


# 创建一个迭代器
class MyNumbers:
    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        index = self.index
        if index <= 5:
            self.index = index + 1
            return index
        else:
            raise StopIteration


myClass = MyNumbers()

for x in iter(myClass):
    print(x, end=' ')
print()


# 生成器 generator 使用了 yield函数 返回迭代器

# 斐波那契数列
def fibonacci(n):
    a, b = 0, 1
    for y in range(n):
        yield a
        a, b = b, a + b


f = fibonacci(10)

for x in f:
    print(x, end=' ')
print()
