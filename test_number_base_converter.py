import pytest

from number_base_converter import to_decimal, from_decimal


def test_to_decimal():
    assert to_decimal("1000", 2) == "8"
    assert to_decimal("ABC", 16) == "2748"


def test_from_decimal():
    assert from_decimal("8", 2) == "1000"
    assert from_decimal("2748", 16) == "ABC"