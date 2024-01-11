#!/usr/bin/env python3
""" this is an annotation module"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This function is for safe_element"""
    if lst:
        return lst[0]
    else:
        return None
