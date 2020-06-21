#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# https://www.runoob.com/python3/python3-list.html
# Python3 列表 | 菜鸟教程e
# demo list 列表 序列的一种
# 序列包含列表和元组
# 与java对比 序列 ~ List; 元组 ~ 数组、Array

# 列表中元素可以是不同类型，和js的数组类似，写法也和js的数组一致
list1 = ['Google', 'Runoob', 1997, 200]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a", "b", "c", "d"]
list4 = ["1", "2", "del", "3"]

print(list1)
print(list2)
print(list3)

# 1、访问列表中的值
# 取一个元素的方式和一样
print("list1[0]: ", list1[0])
# 取多个连续元素冒号分隔，相当于js的arr.slice(1, 5)，包含头不包含尾（索引）
print("list2[1:5]: ", list2[1:5])

# 2、更新列表
# 删除第三个元素（索引2）
del list4[2]
print("删除第三个元素后：", list4)
# 删除一个切割
list_multi_del = [1, 2, 3, 4]
del list_multi_del[1: 3]
print("删除一个切割后：", list_multi_del)

# 3、操作符
print("长度：", len(list1))
print("组合：", list1 + list2)
print("重复：", list3 * 2)
# in操作符js中叫成员操作符
print("存在：", 1997 in list1)
print("存在：", 3 in list2)
# 不同的是Python判断元素是否存在，而js是判断索引是否存在
print("存在：", 3 in list3)
# 迭代
for x in list1:
    print(x, end=" ")

# 4、截取与拼接
L = ['Google', 'Xiaomi', 'Taobao']
# 截取
print("第三个元素：", L[2])
# 倒着取这种方式js和java没有
print("倒数第二个元素：", L[-2])
print("从第二个到结尾：", L[1:])

# 拼接
# print(L += [3, 4, 5]) #错误写法
L += [3, 4, 5]
print("拼接之后：", L)

# 5、嵌套列表
# 就是把其他列表当做另一个列表的元素
list5 = [list1, list2, list3]
print(list5)

# 6、全局函数操作列表
print("len: ", len(list1))
print("max: ", max(list2))
print("min: ", min(list3))
# 元组转换为列表
print("list: ", list(('Java', 'Javascript', 'Python')))

# 7、列表函数
# 追加元素
print("append: ", list1.append(2020))
# 统计元素出现次数
print("count", list2.count(1997))
# 扩展列表
print("extent: ", list3.extend(['ext', 'ent']))
# 找元素索引
print("index: ", list4.index("2"))
# 根据索引插入
print("insert: ", list4.insert(2, "insert"))
# 弹出元素（索引默认-1）并返回该元素
print("pop: ", list3.pop())
print("pop: ", list3.pop(2))
# 移除第一个匹配的元素
print("remove: ", list3.remove("ext"))
# 排序
print("sort: ", list2.sort())
# 清空列表
print("clear: ", list4)
# 复制
print("copy: ", list1.copy())








