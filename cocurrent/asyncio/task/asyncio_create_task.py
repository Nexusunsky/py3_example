import asyncio


async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')

    # Tasks wrap coroutines and track when they are complete.
    task = loop.create_task(task_func())
    print('waiting for {!r}'.format(task))

    return_value = await task
    print('task completed {!r}'.format(task))

    print('return value: {!r}'.format(return_value))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        future = main(event_loop)
        event_loop.run_until_complete(future)
    finally:
        event_loop.close()
