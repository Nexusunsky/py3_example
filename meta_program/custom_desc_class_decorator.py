# 定制描述符的类装饰器

# 问题：实例化描述符时无法得知托管属性（即绑定到描述符上的类属性）的名称。
# 技术方案：
#  1，一旦组建好整个类，而且把描述符绑定到类属性上之后，
#     我们可以审查类，并为描述符设置合理的 存储属性 名称。
#  2，一旦LineItem类构建好，描述符与 托管属性 之间的 绑定 就不会变了，
#     因此，我们要在 创建类时 设置 存储属性 的名称。
# 技术实现：使用类装饰器或元类可以做到这一点.
# 结论：类装饰器 能够 以比较简单的方式 做到 以前需要 元类 去做的事情-----创建类时定制类
# 缺陷：
#     只对直接依附的类有效。这意味着，被装饰的类的子类可能继承也可能不继承装饰其所做的改动，具体情况视改动的方式而定。

from descriptor.bulkfood import bulkfood_pattern
from descriptor.bulkfood.bulkfood_pattern import Validated


# 装饰器参数是一个类
def entity(cls):
    # 迭代存储 类属性 的 字典
    for key, attr in cls.__dict__.items():
        # 如果 属性 是 Validated描述符 的实例
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            # 使用 描述符类的名称 和 托管属性的名称 命名storage_name
            attr.storage_name = '_{}#{}'.format(type_name, key)
    # 返回修改后的类
    return cls


@entity
class LineItem:
    description = bulkfood_pattern.NonBlank()
    weight = bulkfood_pattern.Quantity()
    price = bulkfood_pattern.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    # BEGIN LINEITEM_V6_DEMO
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(dir(raisins)[:3])
    print(LineItem.description.storage_name)
    print(raisins.description)
    print(getattr(raisins, '_NonBlank#description'))
    # END LINEITEM_V6_DEMO
