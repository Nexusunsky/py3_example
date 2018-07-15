import asyncio


async def task_func():
    print('in task_func, sleeping')

    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func was canceled')
        raise

    return 'the result'


def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('canceled the task')


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())  # wrap task_func in task

    loop.call_soon(task_canceller, task)

    try:
        await task
    except asyncio.CancelledError:
        print('main() also sees task as canceled')


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        future = main(event_loop)
        event_loop.run_until_complete(future)
    finally:
        event_loop.close()
