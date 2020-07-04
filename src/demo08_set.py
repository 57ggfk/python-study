#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 集合（set）无序的不重复元素序列
# 相当于java的Set

# 1、创建方式
# {value, ... }方式
set1 = {'value01', 'value02', 3, 4}
print(set1)
# set()方式，把字符串序列中每个字符拆成一个元素
set2 = set('123456')
print(set2)
# 空集合打印出来是set()
set3 = set()
print(set3)
# {} 这种方式是创建空字典
dict4 = {}

# 2、集合的运算
print("2包含在123", '2' in set('123'))

print("3包含在set1", 3 in set1)

print("右边没有的", set('123') - set('234'))

print("两边所有的：", set('123') | set('234'))

print("两边共有的：", set('123') & set('234'))

print("两边特有的：", set('123') ^ set('234'))

# 3、集合内置函数

# 添加元素，返回None
setAdd = set('123')
setAdd.add('4')
print("添加元素：", setAdd)

setAdd.update('5')
print("添加元素：", setAdd)
setAdd.update(set('678'))
print("添加集合：", setAdd)
setAdd.update(['9', '0'])
print("添加集合：", setAdd)
setAdd.update(('a', 'b'))
print("添加集合：", setAdd)
# dict只把key放到set中
setAdd.update({'c': 'v4', 'd': 'v5'})
print("添加集合：", setAdd)

# 移除元素 返回None
setDel = set('12345')
# remove如果不存在会报错
setDel.remove('2')
print("移除2：", setDel)
# discard如果不存在并不会报错
setDel.discard('1')
print("抛弃1：", setDel)
# pop随机弹出
print("随机弹出：", setDel.pop())
print("弹出之后：", setDel)

# 集合长度
print("元素个数：", len(set('12345')))

# 清空集合
print("清空集合：", set('12345').clear())

# 拷贝集合
print("拷贝集合：", set('12345').copy())

# 差集，返回一个新的集合 相当于 -
print("差集：", set('123').difference(set('345')))
print("差集：", set('123') - set('345'))

# 差集，修改原来的集合，无返回值
setDiffUp = set('123')
setDiffUp.difference_update(set('345'))
print("差集更新：", setDiffUp)
print("地址不变：", id(setDiffUp))

# 交集 &
setInter = set('123')
print("交集新集合：", setInter.intersection(set('234')))
setInter.intersection_update(set('345'))
print("交集更新：", setInter)

# 是否没有有交集
print("有交集：", not set('123').isdisjoint(set('345')))
print("没有交集：", set('123').isdisjoint(set('456')))

# 是否参数的子集
print("是参数的子集：", set('123').issubset(set('1234')))
# 是否参数的超集
print("是参数的超集：", set('123').issuperset(set('12')))

# 补集 ^
print("补集：", set('123') ^ set('234'))
setSym = set('123')
print("补集新集合：", setSym.symmetric_difference(set('234')))
setSym.symmetric_difference_update(set('234'))
print("补集更新：", setSym)

# 并集 |
print("并集：", set('123') | set('234'))
setUnion = set('123')
print("并集新集合：", setUnion.union(set('234')))


