#!/usr/bin/env python3
"""
Concurrent coroutines
"""

import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return list of all delays
    """
    lst, fArray = [], []
    for _ in range(n):
        lst.append(wait_random(max_delay))

    for task in asyncio.as_completed(lst):
        result = await task
        fArray.append(result)
    return fArray
