# Task 测试 import 和 运行时的 程序执行顺序：

### ------------Do it myself-------------- ###
# import evaltime
# <[1]> evaltime module start
# <[2]> ClassOne body
# <[7]> ClassThree body
# <[100]> evalsupport module star
# <[200]> deco_alpha
# <[400]> MetaAleph body
# <[700]> evalsupport module en
# <[7]> ClassThree body
# <[9]> ClassFour bod
# <[14]> evaltime module end
### ------------Execute result-------------- ###
# >>> import evaltime
# <[100]> evalsupport module start <1>: 模块中的所有顶层代码在导入模块时运行；解释器会编译deco_alpha函数，但是不会执行定义体
# <[400]> MetaAleph body <2>: MetaAleph类的定义体运行了
# <[700]> evalsupport module end
# <[1]> evaltime module start
# <[2]> ClassOne body <3>: 每个类的定义体都执行了...
# <[6]> ClassTwo body <4>: ...包括嵌套的类
# <[7]> ClassThree body
# <[200]> deco_alpha <5>: 先计算 被装饰的类ClassThree 的定义体，然后运行装饰器函数
# <[9]> ClassFour body
# <[14]> evaltime module end <6>: 在导入场景中main语句块体不会执行
### ------------Attention-------------- ###
# 1，这个场景仅仅由简单的import触发。
# 2，解释器会执行所导入模块及其依赖中的每个类定义体。
# 3，解释器 先计算 类的定义体，然后调用 依附在类上的装饰器函数，这是合理的行为，因为必须先构建 类对象，装饰器才有 类对象 可处理。
# 4，这个场景中，只运行了一个用户定义的函数和方法---deco_alpha装饰器。

### ------------Do it myself-------------- ###
# python3 evaltime.py
# <[11]> ClassOne tests...........................
# <[3]> ClassOne.__init__
# <[5]> ClassOne.method_x
# <[12]> ClassOne tests...........................
# <[300]> deco_alpha:inner_1
# <[13]> ClassOne tests...........................
# <[10]> ClassFour.method_y
### ------------Execute result-------------- ###
# python3 evaltime.py
# <[100]> evalsupport module start
# <[400]> MetaAleph body
# <[700]> evalsupport module end
# <[1]> evaltime module start
# <[2]> ClassOne body
# <[6]> ClassTwo body
# <[7]> ClassThree body
# <[200]> deco_alpha
# <[9]> ClassFour body <1>: 至此，输出与之前一致
# <[11]> ClassOne tests ..............................
# <[3]> ClassOne.__init__ <2>: 类的标准行为
# <[5]> ClassOne.method_x
# <[12]> ClassThree tests ..............................
# <[300]> deco_alpha:inner_1 <3>: deco_alpha装饰器修改了ClassThree.method_y方法，因此调用three.method_y()时运行了inner_1函数的定义体
# <[13]> ClassFour tests ..............................
# <[10]> ClassFour.method_y
# <[14]> evaltime module end
# <[4]> ClassOne.__del__ <4>: 只有程序结束时，绑定在全局变量one上的ClassOne实例才会被垃圾回收程序回收
### ------------Attention-------------- ###
# 类装饰器可能对子类没有影响。
