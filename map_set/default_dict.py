# BEGIN INDEX_DEFAULT
"""Build an index mapping word -> list of occurrences"""

# 实例化一个 defaultdict 的时候需要给构造方法提供一个可调用对象default_factory,
# 它会在 __getitem__ 方法碰到找不到的键的时候被调用 让 __getitem__返回默认值
# 这一切的方法背后是由__missing__支持的，它会在__getitem__里被调用，并在defaultdict遇到找不到的键的时候调用default_factory

import sys
import re
import collections

WORD_RE = re.compile('\w+')

index = collections.defaultdict(list)  # <1> list 的构造方法作为 default_factory 创建一个defaultdict
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)  # <2> default_factory 只会在__getitem__中被调用

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# END INDEX_DEFAULT
