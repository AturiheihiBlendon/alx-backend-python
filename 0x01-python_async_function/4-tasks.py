#!/usr/bin/env python3
"""
Concurrent coroutines
"""

import random
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return list of all delays
    """
    lst, fArray = [], []
    for _ in range(n):
        lst.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(lst):
        result = await task
        fArray.append(result)
    return fArray
