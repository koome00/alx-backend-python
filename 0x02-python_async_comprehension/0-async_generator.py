#!/usr/bin/env python3
"""async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """async generator"""
    i = 0
    while i <= 10:
        val = random.uniform(0, 10)
        yield val
        await asyncio.sleep(1)
        i += 1
