# 导入时 和 运行时 比较

# 元编程 必须知道 Python 解释器什么时候计算各个代码块。
# Python程序员会区分"导入时"和"运行时"：
#       进程中首次导入模块时，还会运行所导入模块的全部顶层代码，
#       以后导入相同的模块则使用缓存，只做名称绑定
#       而这些顶层代码可以做任何事情，包括运行时的工作。
#       由此可知，导入时和运行时之间的界限是模糊的，import 语句可以触发任何"运行时"行为。

# 导入时会"运行全部顶层代码"，但是"顶层代码"会经过一些加工。
# 导入模块时：
#       1，解释器 会执行 顶层的def语句，解释器 会编译 函数的定义体（首次导入模块时）
#       2，把函数对象绑定到对应的全局名称上，但是显然解释器不会执行函数的定义体。
#       3，通常意味着解释器在导入时定义顶层函数，但是仅当在运行时调用函数时才会执行函数的定义体。

# 对类而言，情况不同：
#   在导入时，解释器会执行每个类的定义体，甚至会执行嵌套类的定义体。
#   执行类定义体的结果是，定义了类的属性和方法，并构建了类的对象。
#   类的定义体属于"顶层代码"，因为它在导入时运行。

