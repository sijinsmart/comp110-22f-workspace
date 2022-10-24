"""Exercise04_utils."""

__author__ = "730481811"


def all(x: list[int], y: int) -> bool:
    """Return a bool indicating whether or not all the ints in the list are the same as the given int."""
    i = 0
    result = []
    if len(x) == 0:
        return False
    else:
        while i < len(x):
            if x[i] == y:
                result.append(True)
            else:
                result.append(False)    
            i = i + 1
        if False in result:
            return False
        else:
            return True


def max(x: list[int]) -> int:
    """Return the max interger in the list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    i = 0
    max_value = x[0]
    while i < len(x):
        if x[i] > max_value:
            max_value = x[i]
        else:
            max_value = max_value
        i = i + 1
    return max_value


def is_equal(x: list[int], y: list[int]) -> bool:
    """Return True if every element at every index in equal in both lists."""
    i = 0
    a = []
    if len(x) != len(y):
        return False
    else:
        while i < len(x):
            if x[i] == y[i]:
                a.append(True)
            else:
                a.append(False)
            i = i + 1
        if False in a:
            return False
        else:
            return True