# 使用列表推导实现笛卡尔乘积

if __name__ == '__main__':
    sizes = ['s', 'm', 'l']
    colors = ['black', 'white']
    tshirts1 = [(color, size) for color in colors for size in sizes]
    print(tshirts1)
    tshirts2 = [(color, size) for size in sizes for color in colors]
    print(tshirts2)
