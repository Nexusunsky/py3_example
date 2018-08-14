def record_factory(cls_name, field_names):
    try:
        # <1> 鸭子类型：尝试 在逗号和空格处拆分field_names, 一个元素对应一个属性名
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass

    # <2> 使用属性名构建元组，将成为新建类的__slots__属性，
    # 同时设定了拆包和字符串表示形式中各字段的顺序
    field_names = tuple(field_names)

    # <3> 定义新建类的__init__方法，参数有位置参数和关键字参数。
    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    # <4> 实现__iter__函数，把类的实例变成可迭代的对象，按照__slots__设定的顺序参出字段值
    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    # <5> 迭代__slots__ 和self，将对象self 表示成 友好的字符串表示形式
    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    # <6> 组建类属性字典
    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    # <7> 调用type构造方法，构建新类，然后将其返回
    return type(cls_name, (object,), cls_attrs)


if __name__ == '__main__':
    # BEGIN RECORD_FACTORY_DEMO
    # 工厂函数 的签名与namedtuple类似：
    # 先写类名，后面跟着写在一个字符串里的多个属性名，使用空格和逗号分开
    Dog = record_factory('Dog', 'name weight owner')

    rex = Dog('Rex', 30, 'Bob')
    # 输出友好的字符串表示形式
    print(rex)

    name, weight, _ = rex
    print(name, weight)
    print("{2}'s dog weighs {1}kg".format(*rex))
    rex.weight = 32
    print(rex)
    print(Dog.__mro__)
    # END RECORD_FACTORY_DEMO
