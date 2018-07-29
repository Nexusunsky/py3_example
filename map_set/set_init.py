# Set 在Python中比较年轻，其不可变类型为frozenset，其本质是许多唯一对象的聚集
if __name__ == '__main__':
    l = ['spam', 'spam', 'eggs', 'spam']
    print(set(l))
    print(list(set(l)))

    s = {1}
    print(type(s))

    print(s)

    s.pop()
    print(s) # 空集合使用 set()表示

    # found = len(needles & haystack) 销量更高，更易读
    # < == > 等价于
    # found = 0
    # for n in needles:
    #     if n in haystack:
    #         found += 1
