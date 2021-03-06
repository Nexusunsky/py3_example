import asyncio


def callback(n):
    print('callback {} invoked'.format(n))


async def main(loop):
    print('registering callbacks')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)

    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        co_routine = main(event_loop)
        event_loop.run_until_complete(co_routine)
    finally:
        print('closing event loop')
        event_loop.close()
