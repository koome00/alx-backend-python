#!/usr/bin/env python3
"""handling concurrent tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return the list of all the delays (float values)
    in acsending order
    """
    delays = []
    tasks = []
    while n > 0:
        task = task_wait_random(max_delay)
        delays.append(task)
        n -= 1
    for coro in asyncio.as_completed(delays):
        tasks.append(await coro)
    return tasks
