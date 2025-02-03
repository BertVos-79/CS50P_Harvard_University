import pytest
from twttr import shorten


def test_shorten_no_vowels():
    assert shorten("aeiouAEIOU") == ""


def test_shorten_with_vowels():
    assert shorten("New York") == "Nw Yrk"


def test_shorten_with_numbers():
    assert shorten("hello123") == "hll123"


def test_shorten_printing_in_uppercase():
    assert shorten("HELLO") == "HLL"


def test_shorten_with_punctuation():
    assert shorten("Hello, World") == "Hll, Wrld"


def test_error_integer():
    with pytest.raises(TypeError):
        shorten(4)


def test_shorten_empty_string():
    assert shorten("") == ""


def test_error_float():
    with pytest.raises(TypeError):
        shorten(4.5)
