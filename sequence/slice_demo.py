def get_slice():
    s = 'bicycle'
    s_ = s[::3]
    print(s_)
    print(type(s_))
    print(s[::-1])
    print(s[::-2])


if __name__ == '__main__':
    get_slice()
    l = list(range(10))
    print(l)
    l[2:5] = [20, 30]
    print(l)
    del l[5:7]
    print(l)
    l[3::2] = [11, 22]
    print(l)
    l[2:5] = 100  # 赋值的对象是一个切片，那么赋值语句的右侧也必须是可迭代对象
    print(l)
