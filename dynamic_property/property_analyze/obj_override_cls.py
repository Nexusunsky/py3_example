# 如果 实例 和 所属的类 有同名数据属性，那么实例属性会覆盖类属性


class Test:
    data = ' the class data attr'

    @property
    def prop(self):
        return ' the prop value '


if __name__ == '__main__':
    obj = Test()
    print(vars(obj))  # vars()函数返回 obj 的__dict__()属性

    print(obj.data)  # 读取 obj.data，获取的是Test.data的值

    obj.data = 'bar'  # 为 obj.data赋值，创建了 一个实例属性
    obj.dynamic = 'dyn1'  # 为 obj.dynamic赋值，创建了 一个实例属性
    print(vars(obj))

    print(obj.data)  # 读取的是对象的data，获取的是实例属性的值，从obj实例中 读取属性时，实例属性data会遮盖 属性data

    print(Test.data)
