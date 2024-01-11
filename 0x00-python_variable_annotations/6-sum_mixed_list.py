#!/usr/bin/env python3
""" this is an annotation module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ it returns the sum """
    total = 0
    for val in mxd_lst:
        total += val
    return float(total)
