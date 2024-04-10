!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    ""Adds two integers,
    Args:
        a: the first integer,
        b: the second integer, default 98,

    Raises:
        TypeError: if a, b are not int, float,
    Returns:
        The sum of the two integers.
        """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) is not in (int, float):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
    
