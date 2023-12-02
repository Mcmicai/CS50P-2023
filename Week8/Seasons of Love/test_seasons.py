from seasons import get_minutes

from datetime import date

def test_get_minutes():
    assert get_minutes(date(2003,8,5),date(2023,8,28))==10552320
    assert get_minutes(date(1970,1,1),date(2000,1,1))==15778080