# Write a python program to find the longest words in a file.

with open("textfile.txt", mode="r") as file:
    # getting everything from the file
    content = file.read()

    # splitting words
    all_words = content.split()

    # max length is zero at the start
    max_length = 0

    # list containing the longest words, in case there are multiple
    # with the same length
    longest_words = []

    # go through all the words
    for word in all_words:
        # we remove punctuation (what about \n?)
        word = word.strip('".,!?"')
        # if word is longer than max length
        if len(word) > max_length:
            # set new max length
            max_length = len(word)
            # append word
            longest_words.append(word)
        # in case the
        elif len(word) == max_length:
            # append word
            longest_words.append(word)

# print longest words
print(f"Longest words list: {max(longest_words)}")
