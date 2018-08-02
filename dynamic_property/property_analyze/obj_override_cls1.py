# 如果 实例 和 所属的类 有 同名数据属性，那么 实例属性 会覆盖 类属性
# 而 特性 是 类属性，特性 会覆盖 实例属性


class Test:
    data = ' the class data attr'

    @property
    def prop(self):
        return ' the prop value '


if __name__ == '__main__':
    print(Test.prop)  # 直接从Test 中读取prop属性值，得到的是特性对象本身，不会运行特性的读值方法

    obj = Test()
    print(obj.prop)  # 读取 obj.prop会执行特性的读值方法

    # obj.prop = ' foo'  # 尝试通过 设置prop属性 失败 AttributeError: can't set attribute

    obj.data = 'bar'
    obj.__dict__['prop'] = 'foo'  # 可以直接把 'prop' 存入 obj.__dict__
    print(vars(obj))  # obj此时有两个实例属性 data 和 prop

    print(obj.prop)  # 读取 obj.prop时 仍会 运行特性 的读值方法 特性没有被 实例属性覆盖
    Test.prop = 'baz'  # 覆盖 Test.prop特性，销毁特性对象
    print(obj.prop)  # 现在 obj.prop获取的是实例属性，Test.prop已经不是 特性了，因此不会在覆盖 obj.prop 实例属性
    print('------------------------------')
    print(obj.data)  # obj.data获取的是实例属性data
    print(Test.data)  # Test.data 获取的是类属性 data

    Test.data = property(lambda self: ' the "data" prop value ')  # 使用新特性 覆盖 Test.data
    print(obj.data)  # obj.data被 Test.data特性遮盖

    del Test.data  # 再一次 删除特性
    print(obj.data)  # 恢复 ，obj.data 获取的仍是 实例属性 data

# 本节的主要观点：obj.attr 这样的表达式 不会从 obj 开始寻找attr，而是从 obj.__class__开始
# 而且 ，仅当 类中没有名为attr的特性时，python 才会在obj对象 中寻找
# 这条规则不仅 适用于 特性， 还适用于 一整类 描述符 覆盖型描述符
