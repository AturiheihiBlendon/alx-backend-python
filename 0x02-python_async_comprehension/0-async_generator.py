#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio


async def async_generator():
    for _ in range(10):
        yield random.random()
        await asyncio.sleep(1)
