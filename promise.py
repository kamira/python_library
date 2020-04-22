import asyncio


PROMISE_ALL = "all"
PROMISE_RACE = "race"


class Promised:
    def syncAll(self, tasks: list) -> list:
        return asyncio.run(self.all(tasks))

    def syncRace(self, tasks: list):
        return asyncio.run(self.race(tasks))

    async def all(self, tasks: list) -> list:
        return await asyncio.gather(*tasks)

    async def race(self, tasks: list):
        done, pendding = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for p in pendding:
            p.cancel()
        return done.pop().result()

    async def create(self, coro, jobs: list, promise: str = PROMISE_ALL):
        task_list = [asyncio.create_task(coro(**i)) for i in jobs]
        promise = promise.lower()
        if promise == PROMISE_ALL:
            return await self.all(task_list)
        elif promise == PROMISE_RACE:
            return await self.race(task_list)


Promise = Promised()

async def test(t: int):
    await asyncio.sleep(t)
    return t
    
async def main():
  task = [{'t': i} for i in range(100)]
  a = await Promise.create(test, task, promise=PROMISE_RACE)
  print(a)


if __name__ == "__main__":
    asyncio.run(main())
