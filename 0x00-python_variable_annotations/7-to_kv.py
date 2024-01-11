#!/usr/bin/env python3
""" this is an annotation module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    sqr = v * v
    return (k, sqr)
