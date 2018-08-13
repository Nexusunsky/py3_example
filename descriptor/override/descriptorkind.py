### auxiliary functions for display only ###


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


### essential classes for this example ###

class Overriding:  # <1> 有__get__，__set__的典型覆盖描述符
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)  # <2>

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:  # <3> 没有 __get__方法的覆盖型描述符
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoSet:  # <4>没有__set__方法，所以这是非覆盖型描述符
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:  # <5> 托管类 使用了描述符的实例
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = OverridingNoSet()

    def spam(self):  # <6> spam方法对比，因为方法也是描述符
        print('-> Managed.spam({})'.format(display(self)))


# END DESCR_KINDS


def over_all():
    obj = Managed()  # <1> 创建Managed对象
    # BEGIN DESCR_KINDS_DEMO1
    print(obj.over)  # <2> obj.over触发描述符的__get__方法，第二个参数的值是托管实例obj
    print(Managed.over)  # <3> Managed.over触发描述符的__get__方法，第二个参数（instance）的值是None
    obj.over = 7  # <4> 为obj.over赋值，触发描述符的__set__方法，最后一个参数的值是7
    print(obj.over)  # <5> 读取obj.over，仍会触发描述符的__get__方法。
    obj.__dict__['over'] = 8  # <6> 跳过描述符，直接通过obj.__dict__属性设值
    print(vars(obj))  # <7>
    print(obj.over)  # <8> 即使是名为over 的实例属性，Managed.over描述符仍会覆盖读取obj.over这个操作
    # END DESCR_KINDS_DEMO1


def no_get():
    obj = Managed()  # <1> 创建Managed对象
    # 只有写操作由描述符处理。通过实例读取描述符会返回描述符对象本身，因为没有处理读操作的 __get__ 方法。
    print(obj.over_no_get)  # 因为描述符没有实现__get__方法，因此obj.over_no_get从类中获取描述符实例。
    print(Managed.over_no_get)  # 从托管类中读取描述符实例也是如此。
    obj.over_no_get = 7
    print(obj.over_no_get)  # 因为__set__方法没有修改属性，所以在此读取obj.over_no_get获取的仍是托管类中描述符实例
    obj.__dict__['over_no_get'] = 9  # 通过实例的__dict__属性设置名为 over_no_get
    print(obj.over_no_get)  # 通过__dict__属性设置名为over_no_get的实例属性，over_no_get实例属性会覆盖描述符，但是只有读操作如此
    obj.over_no_get = 7  # 为over_no_get 赋值仍然会走__set__方法
    print(obj.over_no_get)  # 读取时，只要有同名的实例属性，描述符会被遮盖


def no_over():
    obj = Managed()  # <1> 创建Managed对象
    # 没有实现__set__方法的描述符是非覆盖型描述符，如果设置了同名的实例属性，描述符会被覆盖，致使描述符无法处理那个实例的那个属性。
    # 方法是以非覆盖型描述符实现的。
    print(obj.non_over)  # <1> obj.non_over触发描述符的__get__方法，第二个参数的值是obj
    obj.non_over = 7  # <2> “Managed.non_over 是非覆盖型描述符，因此没有干涉赋值操作的 __set__ 方法。”
    print(obj.non_over)  # <3> obj有个名为non_over的实例属性，把Managed类的同名描述符属性遮盖掉。
    print(Managed.non_over)  # <4> “Managed.non_over 描述符依然存在，会通过类截获这次访问。”
    del obj.non_over  # <5> 删除 non_over 实例属性
    print(obj.non_over)  # <6> 读取obj.non_over时，会触发类中描述符的__get__方法


def over_class():
    # 不管 描述符是不是覆盖型，为类属性赋值都能覆盖描述符，这是一种猴子补丁技术
    # 读类属性的操作可以由依附在托管类上定义有__get__方法的描述符处理，
    # 但是写类属性的操作不会由依附在托管类上定义有__set__方法的描述符处理
    # 若想控制设置类属性的操作，要把描述符依附在类的类上，即依附在元类上。
    # 默认情况下，对用户定义的类来说，其元类是type，而我们不能为type添加属性。
    obj = Managed()
    Managed.over = 1
    Managed.over_no_get = 2
    Managed.non_over = 3
    print(obj.over, obj.over_no_get, obj.non_over)


def method_describer():
    # 使用描述符实现方法
    # 解释一个现象： “obj.spam 和 Managed.spam 获取的是不同的对象。”
    # 与描述符一样:
    #   1, 通过托管类访问时，函数的 __get__ 方法会返回自身的引用。
    #   2, 通过实例访问时，函数的 __get__ 方法返回的是绑定方法对象：
    #      一种可调用的对象，里面包装着函数， 并把托管实例（例如 obj）绑定给函数的第一个参数（即 self）
    # 这与 functools.partial 函数的行为一致（参见 5.10.2 节）。
    #
    obj = Managed()
    print(obj.spam)  # <1> obj.spam获取的是绑定方法对象
    print(Managed.spam)  # <2> Managed.spam获取的是函数
    obj.spam = 7  # <3> “如果为 obj.spam 赋值，会遮盖类属性，导致无法通过 obj 实例访问 spam 方法。”
    print(obj.spam)


# BEGIN FUNC_DESCRIPTOR_EX
import collections


class Text(collections.UserString):

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]


# END FUNC_DESCRIPTOR_EX


def bound_function():
    word = Text('forward')
    print(word)  # <1> Text 实例的repr方法返回一个类似Text构造方法调用的字符串，可用于创建相同的实例
    print(word.reverse())  # <2> reverse 方法返回反向拼写的单词
    Text.reverse(Text('backward'))  # <3> 在类上调用方法相当于调用函数
    print(type(Text.reverse), type(word.reverse))  # <4> 注意类型不同，一个是function，一个是method。
    # <5> Text.reverse 相当于函数，甚至可以处理 Text 实例之外的其他对象。
    print(list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])))
    # <6> 函数都是非覆盖型描述符。在函数上调用 __get__ 方法时传入实例，得到的是绑定到那个实例上的方法。
    print(Text.reverse.__get__(word))
    # <7> 调用函数的 __get__ 方法时，如果 instance 参数的值是 None，那么得到的是函数本身。
    print(Text.reverse.__get__(None, Text))
    # <8> word.reverse 表达式其实会调用 Text.reverse.__get__(word)，返回对应的绑定方法。
    print(word.reverse)
    # <9> 绑定方法对象有个 __self__ 属性，其值是调用这个方法的实例引用。
    print(word.reverse.__self__)
    # <10> 绑定方法的 __func__ 属性是依附在托管类上那个原始函数的引用
    print(word.reverse.__func__ is Text.reverse)
    # 结论：
    # 绑定方法对象还有个 __call__ 方法，用于处理真正的调用过程。
    # 这个方法会调用 __func__ 属性引用的原始函数，把函数的第一个参数设为绑定方法的 __self__ 属性。
    # 这就是形参 self 的隐式绑定方式。
    # 函数会变成绑定方法，这是 Python 语言底层使用描述符的最好例证。


if __name__ == '__main__':
    bound_function()
