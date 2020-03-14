def test_inc_one():
    assert inc(3) == 4

def test_inc_two():
    assert inc(0) == 1

def test_inc_three():
    assert inc(-1) == 0

def test_inc_four():
    assert inc(-2) == -1