# Tue Aug 15 20:47:12 2023 - world!
# Tue Aug 15 20:47:13 2023 - Hello

import asyncio 
import time 

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    #start coroutine twice (hopefully they start!)
    first_awaitable = print_after("world!", 2)
    second_awaitable = print_after("Hello", 1)
    # Wait for coroutone to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())