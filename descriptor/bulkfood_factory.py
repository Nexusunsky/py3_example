def quantity():
    try:
        quantity.counter += 1  # 定义函数quantity 自身的属性
    except AttributeError:
        quantity.counter = 0  # 如果 quantity.counter 属性未定义，便初始化值0

    # 使用局部变量 storage_name，借助闭包保持 它的值
    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    # 局部定义的一个函数引用
    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('Value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:  # 托管类
    weight = quantity()
    price = quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    print(LineItem.price)
    br_nuts = LineItem('Brazil nuts', 10, 34.95)
    print(br_nuts.price)
