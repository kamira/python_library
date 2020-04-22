import asyncio

class Promised:
    def all(self, tasks: list) -> list:
        return asyncio.run(self.asyncAll(*tasks))
    
    def race(self, tasks: list):
        return asyncio.run(self.asyncRace(*tasks))
    
    async def asyncAll(self, tasks: list) -> list:
        return await asyncio.gather(*tasks)
    
    async def asyncRace(self, tasks: list):
        done, pendding = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for p in pendding:
            p.cancel()
        return done.pop().result()

Promise = Promised()

def main():
  task = [test(i) for i in range(10)]
  a = Promise.race(task)
  print(a)


if __name__ == "__main__":
    main()
