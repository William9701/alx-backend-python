#!/usr/bin/env python3
""" This is a basic_async module"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
