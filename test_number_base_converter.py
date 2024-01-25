import pytest

from number_base_converter import to_decimal, from_decimal


def test_to_decimal():
    assert to_decimal("1000", 2) == "8"
    assert to_decimal("1000", 8) == "512"
    assert to_decimal("1000", 10) == "1000"
    assert to_decimal("1000", 16) == "4096"
    assert to_decimal("ABC", 16) == "2748"
    assert to_decimal("ABC123", 16) == "11256099"
    assert to_decimal("0", 2) == "0"
    assert to_decimal("0000", 2) == "0"


def test_from_decimal():
    assert from_decimal("8", 2) == "1000"
    assert from_decimal("512", 8) == "1000"
    assert from_decimal("1000", 10) == "1000"
    assert from_decimal("4096", 16) == "1000"
    assert from_decimal("2748", 16) == "ABC"
    assert from_decimal("11256099", 16) == "ABC123"
    assert from_decimal("0", 10) == "0"