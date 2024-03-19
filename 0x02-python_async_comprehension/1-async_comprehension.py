#!/usr/bin/env python3
"""List comprehesion in async"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehesion() -> List[float]:
    """
    List comprehesion in async
    """
    result = [i async for i in async_generator()]
    return result
