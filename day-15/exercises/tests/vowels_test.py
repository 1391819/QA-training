from programs import vowels


# test number of vowels in word
def test_vowels():
    assert vowels.vowels("aeiou") == 5
    assert vowels.vowels("make") == 2
    assert vowels.vowels("mmmmh") == 0
    assert vowels.vowels("AEIOU") == 5
