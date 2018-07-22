# namedtuple 构建的类实例所消耗的内存跟元组一样，因为字段名都存在对应的类里面
# 这个实例跟普通对象实例要小一些，因为python 不会用__dict__来存放这些实例的属性
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])
if __name__ == '__main__':
    print(Card._fields)  # ('rank', 'suit')

    diamonds = Card('2', 'diamonds')
    print(diamonds._asdict())  # OrderedDict([('rank', '2'), ('suit', 'diamonds')])

    clubs_ = ('4', 'clubs')
    print(Card._make(clubs_))  # Card(rank='4', suit='clubs')
