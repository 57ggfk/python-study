#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 面向对象 oop

# 类


class Class:
    pass


# 类的成员：属性和方法


class MyClass:
    """一个简单的类实例"""
    i = 123

    def __init__(self):
        """构造方法"""
        self.data = 456

    def f(self):
        """类的方法"""
        # self代表类的实例
        return 'hello'


# 对象
my = MyClass()
print("访问属性：", my.i)
print("访问方法：", my.f())
print("构造方法初始化的数据：", my.data)


class MyClass2:
    """测试构造方法传参"""
    data = None

    def __init__(self, data):
        """构造方法传参"""
        self.data = data

    def get_data(self):
        return self.data


my2 = MyClass2(789)
print("构造方法传参：", my2.get_data())

# 继承
print("继承>>>")


class BaseClassName:
    def __init__(self):
        print("执行父类1构造方法")


class DerivedClassName(BaseClassName):
    """派生类DerivedClassName继承自BaseClassName"""

    # 不重写构造方法，默认也调了父类的构造方法
    def __init__(self):
        """重写构造方法，需要自己调父类构造"""
        super(DerivedClassName, self).__init__()

    def func(self):
        print("父类1方法")

    def func1(self):
        print("父类1方法1")


DerivedClassName()

# 多继承 有限地支持多继承 只能继承第一个基类的成员，后续基类只能用于调用？
print("多继承>>>")


class BaseClassName2:
    def __init__(self):
        print("执行父类2构造犯法")

    def func(self):
        print("父类2方法")

    def func2(self):
        print("父类2方法2")


class DerivedClassName2(BaseClassName2, BaseClassName):
    """继承了两个基类"""

    # 默认执行第一个父类的构造方法
    def __init__(self):
        """重写构造方法，只能自己调用父类构造方法"""
        # 继承父类构造方式 只能调第一个父类的构造？
        super(DerivedClassName2, self).__init__()
        # 直接调用父类构造方式，和继承构造写法不同，不知道有什么区别？
        BaseClassName.__init__(self)
        BaseClassName2.__init__(self)

    def func(self):
        super(DerivedClassName2, self).func()
        print("重写方法")


dcn2 = DerivedClassName2()
print("测试重写的方法：")
dcn2.func()
dcn2.func2()  # 只能调用第一个继承的基类的方法


# 方法重写

# 私有成员 前缀__  外部不可访问
class DemoVo:
    __name = None
    __age = None

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def name(self):
        return self.__name

    def age(self):
        return self.__age


demo = DemoVo("张三", 18)
print("姓名：", demo.name(), ", 年龄：" + str(demo.age()))

# 专有成员
"""
__init__ : 构造函数，在生成对象时调用()
__del__ : 析构函数，释放对象时使用del
__repr__ : 打印，转换
__setitem__ : 按照索引赋值[]=
__getitem__: 按照索引获取值=[]
__len__: 获得长度len()
__cmp__: 比较运算
__call__: 函数调用.
__add__: 加运算+
__sub__: 减运算-
__mul__: 乘运算*
__truediv__: 除运算、
__mod__: 求余运算%
__pow__: 乘方**
"""


# 运算符重载 重写专有成员
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print("向量相加：", v1 + v2)

