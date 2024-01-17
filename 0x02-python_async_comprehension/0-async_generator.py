#!/usr/bin/env python3
"""This is an asynchronous generator module"""
import asyncio
import random


async def async_generator():
    """This method  that takes no arguments, loops 10 times, each time
    asynchronously waits 1 second, then yields a random number between 0
    and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
