from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("um, um, hello, um") == 3

def test_no_um():
    assert count("hello world") == 0

def test_um_as_part_of_word():
    assert count("yummy umbrella") == 0

def test_case_insensitive_um():
    assert count("Um, UM, um") == 3

def test_um_with_punctuation():
    assert count("um? Um! uM.") == 3

def test_um_with_boundaries():
    assert count("um... uh... um") == 2
