#!/usr/bin/env python3
""" This is a basic_async module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An async function that waits a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
