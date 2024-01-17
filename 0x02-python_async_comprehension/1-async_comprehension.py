#!/usr/bin/env python3
"""This is an asynchronous generator module"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This method takes no arguments, collects 10 random numbers using
    an async comprehension over async_generator, then returns the 10
    random numbers."""
    return [i async for i in async_generator()]
