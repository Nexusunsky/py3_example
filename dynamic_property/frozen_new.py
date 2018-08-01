# 1, 我们通常把__init__方法称之为 构造方法。
# 2, 其实，真正用于构建实例的特殊方法是__new__：这个方法是个类方法，必须返回对象实例（使用了特殊的处理方式，因此不必使用 @classmethod）
# __new__方法返回的对象实例传给了__init__方法，因为调用 __init__方法时要传入实例，并且禁止任何返回值，因此__init__的本质是"初始化方法"
# 3, 真正的构造方法是 __new__，而我们本身不需要自己编写__new__方法，而从object 类继承的实现以及足够了


# Python 构建 对象的过程 可以使用 如下伪代码概括：
from keyword import iskeyword


def object_maker(the_class, some_arg):
    new_object = the_class.__new__(some_arg)
    if isinstance(new_object, the_class):
        the_class.__init__(new_object, some_arg)
    return new_object


# 如下两个构造对象的方法等效
# x = Foo('bar')
# x = object_maker(Foo, 'bar')


# BEGIN EXPLORE2
from collections import abc


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __new__(cls, arg):  # <1> 类方法，第一个参数是类本身，余下的参数和__init__方法一样，只不过没有self
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)  # <2> 默认行为是 委托给 超类的new方法 == > object.__new__(FrozenJSON)
        elif isinstance(arg, abc.MutableSequence):  # <3> __new__方法 中余下的代码 于原先的build方法完全一样。
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])  # <4>
# END EXPLORE2
