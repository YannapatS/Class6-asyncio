# Tue Aug 15 20:48:55 2023 - Hello
# Tue Aug 15 20:48:56 2023 - world!

import asyncio 
import time 

async def print_after(message, delay):
    """"Print a message after thr specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    #Use asyncio.gather to run two coroutine concurrently:
    await asyncio.gather(
        print_after("world!", 2),
        print_after("Hello", 1)    
        )
asyncio.run(main())