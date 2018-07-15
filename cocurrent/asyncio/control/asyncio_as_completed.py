import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.5 - (0.1 * i))
    print('done with phase {}'.format(i))

    return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting for phases to complete')

    results = []
    todo_generator = asyncio.as_completed(phases)
    for future_ in todo_generator:
        answer = await future_  # future.result()
        print('received answer {!r}'.format(answer))
        results.append(answer)

    print('results: {!r}'.format(results))
    return results


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        future = main(3)
        event_loop.run_until_complete(future)
    finally:
        event_loop.close()
