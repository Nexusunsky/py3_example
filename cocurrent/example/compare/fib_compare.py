import threading


# GIL是必须的，这是Python设计的问题：Python解释器是非线程安全的。
# 这意味着当从线程内尝试安全的访问Python对象的时候将有一个全局的强制锁。
# 在任何时候，仅仅一个确定python进程中的单一线程能够获取Python对象或者C API。
# 每100个字节的Python指令解释器将重新获取锁，这（潜在的）阻塞了I/O操作。
# 因为锁，CPU密集型的代码使用线程库时，不会获得性能的提高（但是当它使用之后介绍的多进程库时，性能可以获得提高）。

def time_counter(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))

    return wrapper


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@time_counter
def no_thread():
    fib(35)
    fib(35)


@time_counter
def has_thread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


if __name__ == '__main__':
    no_thread()
    has_thread()
