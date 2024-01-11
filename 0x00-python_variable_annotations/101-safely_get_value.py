#!/usr/bin/env python3
""" this is an annotation module"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """ this is safely value"""
    if key in dct:
        return dct[key]
    else:
        return default
