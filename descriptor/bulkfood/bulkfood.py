class Quantity:  # 描述符类
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
            # setattr(instance, self.storage_name, value) 导致无限递归
        else:
            raise ValueError('Value must be > 0')


class LineItem:  # 托管类
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    truffle = LineItem(' white truffle', 100, 0)
