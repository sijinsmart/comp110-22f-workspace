"""Dictionary exercise."""

__author__ = "730481811"


def invert(x: dict[str, str]) -> dict[str, str]:
    """A function to invert the key and value inside the dictionaries."""
    result: dict[str, str] = dict()
    for i in x:
        if x[i] in result:
            raise KeyError("Duplicate Keys") 
        else:
            result[x[i]] = i    
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Retrun a color that appears most frequently."""
    countdict: dict[str, int] = {}
    for i in x:
        if x[i] in countdict:
            countdict[x[i]] += 1
        else:
            countdict[x[i]] = 1
        item = max(countdict, key=countdict.get)
    return item   


def count(x: list[str]) -> dict[str, int]:
    """Given a list of values will return their numbers in the input list."""
    emptylist: dict[str, int] = {}
    for i in x:
        if i in emptylist:
            emptylist[i] += 1
        else:
            emptylist[i] = 1
    return emptylist