# 描述符 是 多个属性 运用 相同存取逻辑 的一种方式。
# 描述符 是实现了 特定协议的类，这个协议包括__get__，__set__，__delete__方法。
# 实际可仅实现部分描述符号协议
# 描述符的典型用途--管理数据属性。

# property 类实现了完整的描述符协议，
# 除此之外，使用描述符的还有 classmethod 和 staticmethod 装饰器
# 描述符的用法是，创建一个实例，作为一个累的类属性。

# 描述符类：实现描述符协议的类；
# 描述符实例：描述符类的各个实例，声明为托管类的类属性。

# 托管类：把描述符实例声明为类属性的类。
# 托管实例：托管类的实例。

# 托管属性：托管类中由描述符实例处理的公开属性，值存储在存储属性中。
# 储存属性：托管类属性中实际存储，不同于描述符属性，描述符属性都是类属性

# 所列举的式例演示了描述符的典型用途--管理数据属性，这种描述符也叫覆盖性描述符，
# 因为描述符的__set__方法使用托管实例中的同名属性覆盖（接管）要设置的属性。