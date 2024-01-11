#!/usr/bin/env python3
""" this is an annotation module"""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ this is a zoom method """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
