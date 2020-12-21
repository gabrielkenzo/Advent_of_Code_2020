import os
import sys

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "input.txt"))
    lines = file.readlines()
    file.close()
    
    count = 0
    for k in range(len(lines)):
        line = lines[k].split()
        occurrences = line[2].count(line[1][0])
        bounds = line[0].split("-")
        if occurrences in range(int(bounds[0]), int(bounds[1]) + 1):
            count += 1
    print(count)