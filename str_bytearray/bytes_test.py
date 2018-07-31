if __name__ == '__main__':
    cafe = bytes('café', encoding='utf-8')  # bytes 对象从str对象使用给定的编码构建
    print(cafe)
    print(cafe[0])  # 各个元素是rang(256)内的整数
    print(cafe[:1])  # bytes 对象的切片还是bytes对象，即使只有一个字节的切片
    cafe_arr = bytearray(cafe)  # bytearray 没有字面量句法，而是以bytearray()和字节序列字面量参数的形式显示
    print(cafe_arr)
    print(cafe_arr[-1:])  # bytearray 对象的切片还是bytearray对象
