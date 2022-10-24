"""Test for utils functions."""

__author__ = "730481811"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Test for only_even functions."""
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_sub() -> None:
    """Test for sub."""
    x: list[int] = [10, 20, 30, 40]
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == [20, 30]


def test_concat() -> None:
    """Test for concat function."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]