# given a list and an item,
# sum the number of occurances
def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum
