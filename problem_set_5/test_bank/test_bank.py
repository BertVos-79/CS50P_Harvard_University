import pytest
from bank import value


def test_value_0():
    assert value("hello") == 0


def test_value_20():
    assert value("hi") == 20


def test_value_100():
    assert value("what's up") == 100


def test_value_case_insensitive():
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("HeLLo") == 0

