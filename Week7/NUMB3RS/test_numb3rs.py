from numb3rs import validate


def test_validate():
    assert validate("280.1.1.12")==False
    assert validate("hdwad")==False
    assert validate("10.1.10")==False
    assert validate("255.255.266.266")==False
    assert validate("192.168.1.1.1")==False

    assert validate("192.168.1.1")==True
    assert validate("10.10.1.1")==True
    assert validate("255.255.255.255")==True