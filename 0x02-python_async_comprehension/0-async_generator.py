#!/usr/bin/env python3
"""async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator"""
    i = 0
    while i <= 10:
        val = random.uniform(0, 10)
        
        await asyncio.sleep(1)
        yield val
        i += 1
