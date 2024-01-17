#!/usr/bin/env python3
"""This is an asynchronous generator module"""
import asyncio
import time
from typing import List

async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of async_comprehension executed four
    times."""
    start_time = time.time()

    # Use asyncio.gather to execute async_comprehension four times in
    # parallel
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
