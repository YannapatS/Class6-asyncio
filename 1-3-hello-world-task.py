# Tue Aug 15 20:47:50 2023 - Hello
# Tue Aug 15 20:47:51 2023 - world

import asyncio 
import time 

async def print_after(message, delay):
    """"Print a message after thr specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    #start Coroutine twice (hopefully ther start!)
    first_awaitable = asyncio.create_task(print_after("world", 2))
    second_awaitable = asyncio.create_task(print_after("Hello", 1))
    #Wait for coroutines to finish
    await first_awaitable
    await second_awaitable
asyncio.run(main())