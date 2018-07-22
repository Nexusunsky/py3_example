# 生成器表达式遵循了迭代器协议，可以逐个产出元素，而不是先创建一个列表的对象。
# 而生成器这样的惰性求值的方式，可以节省内存
import array


def for_generator():
    """
    生成器实现 for 逐个产出元素
    """
    sizes = ['s', 'm', 'l']
    colors = ['black', 'white']
    for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirts)


def generator_for_init():
    """
    使用生成器来初始化元组和数组
    """
    symbols = '$¢£¥€¤'
    print(tuple(ord(symbol) for symbol in symbols))
    print(array.array(('i'), (ord(symbol) for symbol in symbols)))


if __name__ == '__main__':
    generator_for_init()
    for_generator()
