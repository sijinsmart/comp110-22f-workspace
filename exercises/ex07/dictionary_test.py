"""The test for dictionary function."""

__author__ = "730481811"

from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Test for invert function."""
    x: dict[str, str] = {
        "a": "b",
        "c": "d"
    }
    assert invert(x) == {"b": "a", "d": "c"}


def test_favorite_color() -> None:
    """Test for favorite_color function."""
    x: dict[str, str] = {
        "a": "blue",
        "b": "violet",
        "c": "blue"
    }
    assert favorite_color(x) == "blue"


def test_count() -> None:
    """Test for count function."""
    x: list[str] = []
    assert count(x) == {}