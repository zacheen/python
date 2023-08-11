import asyncio

# asyncio 可以執行 async 宣告的 function
async def main():
    print(1)
asyncio.run(main())

# cache_update_loop 只會執行 6 次程式就會結束(還沒研究)
from discord.ext import tasks
class Cache:
    def __init__(self):
        self.cache_update_loop.start()
        print('__init__')

    @tasks.loop(seconds=3.0)
    async def cache_update_loop(self):
        print(1)

    @cache_update_loop.before_loop
    async def before_cache_update_loop(self):
        print('before loop')

async def main():
    cache = Cache()
    await asyncio.sleep(15)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())