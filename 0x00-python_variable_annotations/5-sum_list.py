#!/usr/bin/env python3
""" this is an annotation module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ it returns the sum """
    total = 0
    for val in input_list:
        total += val
    return total
