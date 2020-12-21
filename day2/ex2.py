import os
import sys

file = open(os.path.join(sys.path[0], "input.txt"))
lines = file.readlines()
count = 0
for k in range(len(lines)):
    line = lines[k].split()
    letter = line[1][0]
    occurrences = line[2].count(letter)
    index = line[0].split("-")

    #XOR condition
    if (line[2][int(index[0]) - 1] == letter) is not (line[2][int(index[1]) - 1] == letter):
        count += 1
print(count)