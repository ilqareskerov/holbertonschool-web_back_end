#!/usr/bin/env python3
"""type-annotated function add that takes a float a
and a float bas arguments and returns their sum as a float"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Use the random module"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return (delay)

