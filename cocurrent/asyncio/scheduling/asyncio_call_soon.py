import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print('callback invoked with {} and {}'.format(arg, kwarg))


async def main(loop):
    print('registering callbacks')
    loop.call_soon(callback, 1)

    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, 2)

    await asyncio.sleep(0.1)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        co_routine = main(event_loop)
        event_loop.run_until_complete(co_routine)
    finally:
        print('closing event loop')
        event_loop.close()
