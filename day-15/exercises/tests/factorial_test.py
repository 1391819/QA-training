from programs import factorial


# return the factorial of a number
def test_fact():
    # factorial of 0 is 1
    assert factorial.fact(0) == 1
    assert factorial.fact(5) == 120
