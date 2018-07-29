# dict 的多种构造方法
if __name__ == '__main__':
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'two': 2, 'one': 1})
    print(a == b == c == d == e)
