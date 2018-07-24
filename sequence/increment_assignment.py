# 增量赋值： += and *=

# += 背后的特殊方法是 __iadd__ : 用于就地加法
# 如果 某个类没有实现 这个方法，就会退一步调用 __add__

if __name__ == '__main__':
    l = [1, 2, 3]  # 对于 list , bytearray , array.array 来说 a 会就地改动 就像调用了a.extend(b)
    print(l)
    print(id(l))

    l *= 2
    print(l)
    print(id(l))

    t = (1, 2, 3)  # 而对于没有实现__iadd__ 方法的不可变类型而言 就会计算得到一个新的对象然后赋值给原引用 a
    print(t)
    print(id(t))

    t *= 2
    print(t)
    print(id(t))
