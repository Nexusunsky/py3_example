import asyncio


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()

    print('scheduling mark_done')
    loop.call_soon(mark_done, all_done, 'the result')

    result = await all_done  # <==> all_done.result()
    print('returned result: {!r}'.format(result))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        co_routine = main(event_loop)
        event_loop.run_until_complete(co_routine)
    finally:
        event_loop.close()
