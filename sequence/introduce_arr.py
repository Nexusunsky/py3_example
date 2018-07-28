# 数组：因为数组背后存放的并不是数据对象，而是数字的机器翻译，也就是字节表述。 同C语言中数组一致
# 如果需要频繁的先进先出，deque（双端队列）速度会更快
# 如果代码里面，包含操作（检查一个元素是否出现在一个集合中）的频率很高，用set（集合）更合适。

# 数组支持所有跟序列有关的操作，另外 数组还提供了从文件读取和存入文件的更快的方法
# Python数组跟C语言数组一样精简，创建数组需要一个类型码，这个类型码用来表示在底层的C语言存放怎样的数据类型
# 例如 array('b)创建出的数组就只能存放一个字节大小的整数，范围从 -128 到 127
# Python 不会允许你从数组存放知道类型之外的数据
from array import array
from random import random

if __name__ == '__main__':
    floats = array('d', (random() for i in range(10 ** 7)))  # 双精度浮点数组
    print(floats[-1])

    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    floats1 = array('d')
    fp = open('floats.bin', 'rb')
    floats1.fromfile(fp, 10 ** 7)  # 从文件floats.bin读取1000万个浮点数
    fp.close()

    print(floats1[-1])
    print(floats1 == floats)

# 另外 一个快速序列化数组类型的方法是pickle
