"""List utils functions."""

__author__ = "730481811"


def only_evens(x: list[int]) -> list[int]:
    """Return only the even elements of the input parameter."""
    result: list[int] = []
    for i in x:
        if i % 2 == 0:
            result.append(i)
    return result


def concat(x: list[int], y: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    result: list[int] = []
    for i in x:
        result.append(i)
    for i in y:
        result.append(i)
    return result


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Return a list which is a subset of the given list, between the specified start index and the end index -1."""
    result: list[int] = []
    if len(x) < 0 or y > len(x) or z <= 0:
        return result
    elif y < 0:
        y = 0
    elif z > len(x):
        z = len(x)
    while y < len(x) and y < z:
        result.append(x[y])
        y = y + 1
        
    return result