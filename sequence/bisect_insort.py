import bisect
import random

SIZE = 7
# 将 元素 插入到序列中并保持 有序性
random.seed(1729)
if __name__ == '__main__':
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)
