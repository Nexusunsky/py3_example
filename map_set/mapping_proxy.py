# 代理实现 不可变字典类型
from types import MappingProxyType

if __name__ == '__main__':
    d = {1: "A"}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    # d_proxy[2] = 'B' TypeError: does not support
    d[2] = 'B'

    print(d_proxy[2])
