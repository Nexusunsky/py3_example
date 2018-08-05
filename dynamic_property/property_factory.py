def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError(' value must be > 0 ')

    return property(qty_getter, qty_setter)


class LineItem:
    # 特性是类属性，构建两个quantity对象时 要传入 LineItem 实例属性 名称，让特性管理
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    nutmeg = LineItem("Moluccan nutmeg", 8, 13.95)

    #  nutmeg 的每个引用 都由 特性函数处理
    # 只有直接存取__dict__属性才能跳过特性的处理逻辑
    print(nutmeg.weight, nutmeg.price)

    print(sorted(vars(nutmeg).items()))
