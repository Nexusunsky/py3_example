# 正文：
#
# 一. 内容回顾
# 1.1 字符问题
# 一个字符串是一个字符序列，问题出在“字符”的定义上。把码位转换成字节序列的过程是编码（encode），把字节序列转换成码位的过程是解码（decode）。
# 在编码和解码过程中就存在Unicode，UTF-8, ASCII等这些方式，导致出现问题，编码格式不一致。
#
# 1.2 字节概要
# 主要讲解字节的结构体和内存视图，分bytes, bytemarray, memory view, array.array。
#
# 1.3 基本的编解码器
# Python自带超过100种编解码器，常见的就是utf-8， gb2313。其中gb2313用于编码简体中文的陈旧的标准，这是亚洲语言中使用较广泛的多字节编码之一。
#
# 1.4 了解编解码问题
# 编解码问题有3个，分别是：UnicodeEncodeError UnicodeDecodeError SyntaxError
# 出现编解码上述3个问题的地方主要是国际化使用，如：处理希腊文，俄文等，出现一些特殊字符。
#
# 1.5 处理文本文件
# 处理文本的最佳实践是：Unicode三明治
# 这里写图片描述
#
# 1.6 为了正确比较而规范化Unicode字符串
# 同上了解编码问题，主要是处理国际化字符问题，进行规范化Unicode字符串。
#
# 1.7 Unicode文本排序
# 文本排序主要是sorted() 和.sort()内置函数的使用。
#
# 1.8 Unicode数据库
#
# 1.9 支持字符串和字节序列的双模式API
# 获取系统编解码方式：locale.getpreferredencoding()、sys.getfilesystemencodeing()。
