from collections import abc

from dynamic_property.osconfeed import load


class FrozenJson:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJson.build(self.__data[name])

    # 常用于备选的构造方法
    @classmethod
    def build(cls, arg):
        if isinstance(arg, abc.Mapping):
            return cls(arg)
        elif isinstance(arg, abc.MutableSequence):
            return [cls.build(item) for item in arg]
        else:
            return arg


if __name__ == '__main__':
    raw_feed = load()
    feed = FrozenJson(raw_feed)
    print(len(feed.Schedule.speakers))
    print(sorted(feed.Schedule.keys()))

    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    print(talk.flavor)
