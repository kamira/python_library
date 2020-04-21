import asyncio


async def promise_all(func: list) -> list:
    return await asyncio.gather(*func)
    

async def test_print(x):
    await asyncio.sleep(0.001)
    print(x)
    return True


def main():
    task = [test_print(i) for i in range(10)]
    print(asyncio.run(promise_all(task)))


if __name__ == "__main__":
    main()
