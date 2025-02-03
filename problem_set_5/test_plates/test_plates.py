import pytest
from plates import is_valid


def test_starts_with_two_letters():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False
    assert is_valid("123AB") == False


def test_plate_length():
    assert is_valid("AB") == True
    assert is_valid("ABCDE") == True
    assert is_valid("ABC123") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_numbers_at_end():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
    assert is_valid("AA1234") == True


def test_no_punctuation():
    assert is_valid("ABC123") == True
    assert is_valid("AB.C12") == False  # Invalid period
    assert is_valid("AB C12") == False  # Invalid space
    assert is_valid("AB,C12") == False  # Invalid comma
