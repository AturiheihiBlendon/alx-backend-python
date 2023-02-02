#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier
    """
    def func(number: float):
        """
        function to be returned
        """
        return number * multiplier
    return func
