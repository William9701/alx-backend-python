#!/usr/bin/env python3
""" This is a basic_async module"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This is the ait_random method"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for i in asyncio.as_completed(tasks):
        delay = await i
        delays.append(delay)
    return delays
