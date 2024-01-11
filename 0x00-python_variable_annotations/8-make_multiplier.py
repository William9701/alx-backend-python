#!/usr/bin/env python3
""" this is an annotation module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplier func"""
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
