import asyncio

Promise = Promised()

class Promised:
  async def all(self, tasks: list) -> list:
    return await asyncio.gather(*taks)

  async def race(self, tasks: list):
    done, pendding = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for p in pendding:
        p.cancel()
    return done.pop().result()

def main():
  task = [test(i) for i in range(10)]
  a = asyncio.run(Promise.race(task))
  print(a)


if __name__ == "__main__":
    main()
