# open the file
file = open("filename.txt", "r")

# data that we will keep
outfile = ""

for line in range(1, 10):
    # skip the lines which are odd
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

# Replace the file
file = open("filename.txt", "w")
file.write(outfile)
file.close()
