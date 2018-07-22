# 使用 *来处理剩下的元素


def get_div_mod():
    print(divmod(20, 8))
    t = (20, 8)
    print(divmod(*t))


def get_rest():
    a, b, *rest = range(5)
    print(a, b, rest)


if __name__ == '__main__':
    get_div_mod()
    get_rest()
