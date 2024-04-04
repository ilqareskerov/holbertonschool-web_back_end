#!/usr/bin/env python3
''' Description: asynchronous coroutine that takes in an integer argument
                 (max_delay, with a default value of 10) named wait_random
                 that waits for a random delay between 0 and max_delay
                 (included and float value) seconds and eventually returns it
    Arguments: max_delay: int = 10
'''

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random
from typing import List
async def wait_n(n: int =0, max_delay: int = 10) -> List[float] :
    """
    float time random
    """
    delays: List[float] = []
    tasks: List = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for i in asyncio.as_completed(tasks):
        result = await i
        delays.append(result)
    return delays

