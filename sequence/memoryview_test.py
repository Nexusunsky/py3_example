# memoryview是一个内置类，让用户再不复制内容的情况下操作同一个数组的不同切片
# 内存视图可以在不复制内容的前提下，在数据结构之间共享内存，其中数据结构可以是任意形式
# memoryview.cast 的概念和数组模块类似 能用不同的方式读写同一块内存数据，而且内容字节不会随意移动

from array import array

if __name__ == '__main__':
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])
    memv_oct = memv.cast('B')  # 创建一个memv_oct把 memv 里的内容转换成'B'类型：无符号字符
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)
