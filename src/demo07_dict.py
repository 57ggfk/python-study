#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# demo dict 字典
# https://www.runoob.com/python3/python3-dictionary.html
# Python3 字典 | 菜鸟教程
# java中的map js中的json

# 写法
d = {"key1": "value1", "key2": "value1"}
print(d)
# key是唯一的，value不是
d2 = {1: "value", "1": "value2", 1: "value3"}
print(d2)

d3 = {None: "None", False: "False", True: "True"}
print(d3)

# 1、取值
# dict[key] 与序列类似，不同的是[]里面是key。js比较灵活支持[]和.两种方式
print(d['key1'])
# 取不存在的key会报错，像java中的JsonObject一样纠错
# print(d['key0'])

# 2、修改
d["key2"] = 'update2'
print("修改key2：", d)
d["key3"] = 'add3'
print("添加key3: ", d)

# 3、删除
# 与js操作类型
del d["key3"]
# 不能删除不存在的key
# del d["key4"]
# 清空
dc = {'key': 'value'}
dc.clear()
# 删除字典
dD = {}
del dD

# 4、字典特征
# key不可重复，后面的会覆盖前面的，与java、js原则类似
print({"1": "value1", "1": "value2"})
# key不可变，key必须使用不可变类型比如数字、字符串或元组，而列表就不行
print({1: "value1", "2": "2", (3,): "3"})

# 5、全局函数操作字典
print("len: ", len(d))
print("str: ", str(d))
print("type: ", type(d))

# 6、字典函数
print("clear: ", d3.clear())
print("copy: ", d2.copy())
# 以seq序列为key创建字典，不知道为啥value都为None
print("fromkeys: ", d.fromkeys(['key1', 'key4']))

print("get: ", d.get("key1"))
print("get None: ", d.get("key0"))
# get与中括号取法不同，key不存在不报错
print("get default: ", d.get("key0", "123"))

# 成员判断
print("key in dict: ", "key1" in d)

# 遍历，返回键值对元组
print("items: ", d.items())

# 遍历keys
print("keys: ", d.keys())

# 遍历values
print("values: ", d.values())

# 不存在则添加
print("setdefault: ", d.setdefault("key5", "value5"))

# 更新值，把别的字段加入此字典，类比java里map.putAll
print("update", d.update({"key6": "value6"}))

# 弹出键值对实体，指定key返回value
print("before pop: ", d)
print("pop: ", d.pop("key6"))
print("after pop: ", d)
print("pop not exists: ", d.pop("key7", "default"))

# 弹出最后一个实体
print("popitem: ", d.popitem())
