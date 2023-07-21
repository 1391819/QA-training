# Write a Python program to count the frequency of words in a file.

# to store words and frequency we can use a dict
frequency = {}

with open("textfile.txt", mode="r") as file:
    for line in file:  # go through each line
        words = line.split()  # we split the line
        for word in words:
            # here we should do some more word cleaning (remove special chars, convert to lower case, etc)
            # this is pretty basic
            clean_word = "".join(word.strip(".!,?")).lower()

            # check if it is an actual word
            if clean_word:
                # update frequency dict - return value of word, and add 1
                # 0 is returned if the word is not in the dict
                frequency[clean_word] = frequency.get(clean_word, 0) + 1

# there are definitely other ways to print the dict in a prettier way
print(f"Words and their frequencies in the file is: {frequency}")
