import struct

# struct 模块提供了一些函数，把打包的字节序列转换成不同类型字段组成的字节序列。
# memoryview 对象允许在二进制数据结构之间共享内存，如果想从二进制序列中提前结构化信息

if __name__ == '__main__':
    fmt = '<3s3sHH'  # 结构体格式 < 是小字节序列，3s3s是两个3字节序列，HH是两个16位二进制整数
    with open('filter.gif', 'rb') as fp:
        img = memoryview(fp.read())  # 使用内存中文件内容创建一个memoryview 对象

    header = img[:10]  # 在使用它的切片在创建一个memoryview 对象，这里不会复制字节序列
    print(header)
    print(struct.unpack(fmt, header))  # 拆包 memoryview 对象，得到一个元组 包含 类型，版本，宽度和高度
    del header
    del img  # 删除引用，释放memoryview对象占用的内存
