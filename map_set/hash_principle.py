# Hash 原理
# 散列表 是一个稀疏数组(总是有空白元素的数组称为稀疏数组)，其中的单元叫做 表元（bucket）在dict的散列表中，每个键值对都占用一个表元
# 每一个表元都有两部分，一个是对键的引用，另一个是对值的引用，因为所有表元大小一致，那么可以通过偏移量来读取某个表元
# python 设法保证大概三分之一的表元是空的，所以会不停有元素被复制到一个更大的空间里面。

# 为了获取my_dict[search_key] 背后的值，python首先调用hash(search_key)计算search_key 的散列值，把这个值最低的几位数当作偏移量，
# 在散列表里查找表元(具体极为取决于散列表的大小)，若找到的表元是空的，抛出KeyError异常，
# 若不是空的，则表元里会有一对found_key:found_value。这时候 python 会检验search_key == found_key 是否为真如果相等就返回found_value
# 如果search_key 和 found_key 不匹配称为散列冲突，算法会 在散列值中另外取几位，然后用特殊的方法处理一下，把新得到数字在当作索引来寻找表元，重复之前步骤


# Set 的实现以及导致的结果：
# Set 和 frozenset 的实现依赖 散列表 但在它们的散列表里存放的只有元素的引用
# 1，集合里的元素必须是可散列的
# 2，很消耗内存
# 3，可以很高效地判断元素是否存在于某个集合
# 4，元素的次序取决于被添加到集合的次序
# 5，往集合里添加元素可能会改变集合已有元素的次序


# dict 的实现及其导致的结果
# 1， 键必须是可散列的：
# 一个可以散列的对象必须满足如下条件：
# 1）支持hash()函数，并且通过__hash__()方法所得到的散列值是不变的。
# 2）支持通过__eq__()来检查相等性
# 3）若 a == b 为真，则hash(a) == hash(b) 也为真
# 4）用户定义的对象默认都是可散列的，其散列值由 id() 来获取 而且它们也是不相等的。


# 2， 字典在内存上的开销巨大
# 稀疏的散列表，如果需要减少内存可使用 元组或是具名元组


# 3， 键查询很快
# 4， 键的次序取决于添加顺序
# 5， 往字典里添加新的键可能会改变已有键的顺序


# BEGIN DIALCODES
# dial codes of the top 10 most populous countries
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

d1 = dict(DIAL_CODES)  # <1> 原样排序
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))  # <2> 区号排序
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))  # <3> 国家名称首字母排序
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3  # <4> 包含的数据一致，则字典相等，与key的顺序无关
# END DIALCODES
"""
# BEGIN DIALCODES_OUTPUT
d1: dict_keys([880, 1, 86, 55, 7, 234, 91, 92, 62, 81])
d2: dict_keys([880, 1, 91, 86, 81, 55, 234, 7, 92, 62])
d3: dict_keys([880, 81, 1, 86, 55, 7, 234, 91, 92, 62])
# END DIALCODES_OUTPUT
"""
