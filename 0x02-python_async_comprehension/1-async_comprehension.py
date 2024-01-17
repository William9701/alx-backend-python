#!/usr/bin/env python3
"""This is an asynchronous generator module"""


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """This method takes no arguments, collects 10 random numbers using
    an async comprehensing over async_generator, then returns the 10
    random numbers."""
    random_numbers = []
    # Using 'async for' to iterate over the async_generator
    async for value in async_generator():
        random_numbers.append(value)
    return random_numbers
