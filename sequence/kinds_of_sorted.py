# 基础排序 : list.sort 和 sorted


def basic_sorted_sort():
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(fruits)
    print(sorted(fruits))
    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=len, reverse=True))
    fruits.sort()
    print(fruits)


if __name__ == '__main__':
    basic_sorted_sort()
