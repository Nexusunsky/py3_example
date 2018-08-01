"""
Handle keywords by appending a `_`.
# BEGIN EXPLORE1_DEMO
    >>> grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    >>> grad.name
    'Jim Bo'
    >>> grad.class_
    1991
# END EXPLORE1_DEMO
"""

from collections import abc
import keyword


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    # BEGIN EXPLORE1
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                # <1> 导入 KeyWord 模块方便我们识别关键字，
                # 与此类似 str的 s.isidentifier()方法能根据语言的语法判断S 是否为有效的 Python的标识符
                key += '_'
            self.__data[key] = value

    # END EXPLORE1
    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:  # <8>
            return obj
