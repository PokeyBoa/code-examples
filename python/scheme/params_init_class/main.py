#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from utils.full_args_class import FullArgsClass
from utils.kwargs_class import KwargsClass


def unit_test1():
    print("\n单元测试1: ")
    # print(FullArgsClass.__doc__)
    # 实例化对象
    args = ["option1", "option2", "option3"]
    kwargs = {"foo": "value1", "bar": "value2"}
    obj = FullArgsClass('number1', 'number2', 'number3', *args, **kwargs)
    # 使用keys方法，获取val列表
    obj.keys()
    # 测试对象属性的获取
    print("结果: ")
    print("1. %s 固定位置参数中 %s 实例变量的值为 %s" % ("fixed", "obj.x", obj.x))
    print("2. {0} 可变元祖参数中 {1} 实例变量的值为 {2}".format("*args", "obj.args01", obj.args01))
    print(f"3. **kwargs 可变map键值对参数中 obj.foo 实例变量的值为 {obj.foo}")


def unit_test2():
    print("\n单元测试2: ")
    # print(KwargsClass.__doc__)
    kwargs = {"foo": "value1", "bar": "value2"}
    obj = KwargsClass(**kwargs)
    # Use the 'keys' method to get a list of vals.
    print(obj.keys)
    # Get test object properties
    print(f"**kwargs The value of the obj.foo instance variable in\n"
          f"the variable map key-value pair parameter is {obj.foo}.")


if __name__ == '__main__':
    unit_test1()
    unit_test2()

