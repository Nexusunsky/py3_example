import asyncio


# The tasks created by gather are not exposed, so they cannot be cancelled.
# The return value is a list of results in the same order as the arguments passed to gather(),
# regardless of the order the background operations actually completed.

async def phase1():
    print('in phase1')
    await asyncio.sleep(2)
    print('done with phase1')
    return 'phase1 result'


async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')
    results = await asyncio.gather(
        phase1(),
        phase2(),
    )
    print('results: {!r}'.format(results))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        future = main()
        event_loop.run_until_complete(future)
    finally:
        event_loop.close()
