#!/usr/bin/env python3
"""
Async Comprehensions
"""
from time import time
import asyncio


async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    returns total executation time
    """
    start = time()
    await asyncio.gather(
        async_comp(),
        async_comp(),
        async_comp(),
        async_comp()
    )
    stop = time()
    return stop - start
