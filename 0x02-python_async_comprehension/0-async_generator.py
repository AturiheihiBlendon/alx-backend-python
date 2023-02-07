#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    yields a random number each time a coroutine is run
    """
    for _ in range(10):
        yield random.random()
        await asyncio.sleep(1)
