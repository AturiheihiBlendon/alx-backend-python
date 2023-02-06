#!/usr/bin/env python3
"""
Measure runtime
"""
import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns total time for execution
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    stop = time()
    return (stop - start) / n
