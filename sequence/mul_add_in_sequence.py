def attention():
    l = ['test']
    print(repr(l))
    my_list = [l] * 3  # 注意：⚠️ ：序列里面的元素是对可变对象的引用，得到的结果是其实是 包含有三个指向同一个对象引用的列表
    for item in my_list:
        print(repr(item))


def list_com_for_mult():
    """
     建立有列表组成的列表最好的方式是使用列表推导
    """
    board = [['_'] * 3 for _ in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)

    # < == > 本质上等价于 如下代码：
    board = []
    for _ in range(3):
        row = ['_'] * 3
        board.append(row)
    print(board)
    board[1][2] = 'X'
    print(board)


def trap_of_mult_in_list():
    """
    陷进：使用 * 来运算元素为引用的列表
    """
    board = [['_'] * 3] * 3
    print(board)
    board[1][2] = 'X'
    print(board)

    # < == > 本质上等价于 如下代码：

    row = ['_'] * 3
    board = []
    for _ in range(3):
        board.append(row)
    print(board)
    board[1][2] = 'X'
    print(board)


# 对序列使用 + 和 * 号
if __name__ == '__main__':
    attention()
    list_com_for_mult()
    trap_of_mult_in_list()
