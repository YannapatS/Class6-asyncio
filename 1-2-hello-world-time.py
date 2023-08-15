# Tue Aug 15 20:47:27 2023 - start of : First Call
# Tue Aug 15 20:47:28 2023 -end of : First Call
# Tue Aug 15 20:47:28 2023 - start of : Second Call
# Tue Aug 15 20:47:29 2023 -end of : Second Call

import asyncio
import time 

async def example(message):
    print(f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print (f"{time.ctime()} -end of :", message)

async def main():
        #start Coroutine twice (hopefully ther start!)
        first_awaitable = example("First Call")
        second_awaitable = example("Second Call")
        #Wait for coroutines to finish
        await first_awaitable
        await second_awaitable
asyncio.run(main())