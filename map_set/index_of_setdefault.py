# BEGIN INDEX0
"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])  # <1>
            occurrences.append(location)  # <2>
            index[word] = occurrences  # <3>

# print in alphabetical order
for word in sorted(index, key=str.upper):  # <4>
    print(word, index[word])
# END INDEX0

# BEGIN INDEX
"""Build an index mapping word -> list of occurrences"""
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)
            # <1> < == >
            # if key not in index:
            #     index[key] = []
            # index[key].append(new_value)

        # print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# END INDEX
