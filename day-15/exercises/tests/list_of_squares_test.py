from programs import list_of_squares


# return a list of n squares in a dict
def test_list_of_squares():
    assert list_of_squares.list_of_squares(1) == {1: 1}
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}
