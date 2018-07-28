from collections import deque

if __name__ == '__main__':
    dq = deque(range(10), maxlen=10)
    print(dq)

    dq.rotate(3)  # 队列最右边的3个元素 会被移动到队列的左边
    print(dq)

    dq.rotate(-4)  # 队列最左边的四个元素会被移动到队列的右边
    print(dq)

    dq.appendleft(-1)  # 视图 对一个已满队列做尾部添加操作的时候，其头部元素会被删除
    print(dq)

    dq.extend([11, 22, 33])
    print(dq)

    dq.extendleft([10, 20, 30, 40])  # 当从左边逐个添加元素时，迭代器里的元素会逆序出现在队列
    print(dq)
