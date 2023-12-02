from um import count

def test_count():
    assert count("hello")==0
    assert count("yummy")==0
    assert count("umu")==0

    assert count("hello, um, world")==1
    assert count("um um")==2
    assert count("um?")==1
    assert count("Um, thanks, um..")==2