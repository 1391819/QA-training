import count


# test function against integers
def test_count_zeros():
    assert count.count([0, 0, 0], 0) == 3
    assert count.count([1, 2, 3, 4, 1, 1, 1], 1) == 4


# test function against strings
def test_count_string():
    assert count.count(["a", "a", "a"], "a") == 3
