# 使用字节序列构建正则表达式，\d 和 \w 等模式 只能匹配 ASCII字符
# 如果是字符串模式 就能匹配ASCII 之外的 Unicode数字或字母
#


# BEGIN RE_DEMO
import re

re_numbers_str = re.compile(r'\d+')  # <1> 字符串类型的正则表达式
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')  # <2> 字节序列类型 正则表达式
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # <3> 
            " as 1729 = 1³ + 12³ = 9³ + 10³.")  # <4>

text_bytes = text_str.encode('utf_8')  # <5> 字节序列 只能用字节序列正则表达式搜索

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))  # <6> 字符串模式 能匹配泰米尔数字 和 ASCII数字
print('  bytes:', re_numbers_bytes.findall(text_bytes))  # <7> 字节序列模式 只能用字节正则表达式 搜索
print('Words')
print('  str  :', re_words_str.findall(text_str))  # <8> 字符串模式 能匹配 字母，上标，泰米尔数字和ASCII数字
print('  bytes:', re_words_bytes.findall(text_bytes))  # <9> 字节序列模式 只能匹配ASCII字节中的字母和数字
# END RE_DEMO
