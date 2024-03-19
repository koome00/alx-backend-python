#!/usr/bin/env python3
"""async generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """async generator"""
    i = 0
    while i < 10:
        val = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield val
        i += 1
