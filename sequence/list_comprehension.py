# list_comprehension 列表推到
# 比较四种迭代获取结果列表的性能
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""
symbols = '$¢£¥€¤'


def non_ascii(c):
    return c > 127


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


if __name__ == '__main__':
    clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
    clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
    clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
    clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
