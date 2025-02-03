from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_ips():
    assert validate("275.3.6.28") == False
    assert validate("192.168.0.256") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.0.1") == False
    assert validate("192.168.-1.1") == False
    assert validate("999.999.999.999") == False

def test_non_numeric():
    assert validate("abc.def.ghi.jkl") == False
    assert validate("123.456.789.xyz") == False
    assert validate("192.168.one.1") == False
