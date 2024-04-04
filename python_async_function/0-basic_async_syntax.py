#!/usr/bin/env python3
"""type-annotated function add that takes a float a
and a float bas arguments and returns their sum as a float"""

import random

async def wait_random(max_delay: int = 10) -> float:
    return random.randint(0, max_delay)
