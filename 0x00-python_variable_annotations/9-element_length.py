#!/usr/bin/env python3
""" this is an annotation module"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element lenght"""
    return [(i, len(i)) for i in lst]


print(element_length.__annotations__)
