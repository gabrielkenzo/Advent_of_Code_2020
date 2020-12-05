from ex1 import find_complement
import os
import sys

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "input.txt"))
    lines = []
    for line in file:
        lines.append(int(line))
    
    for number in lines:
        ret = find_complement(lines, 2020 - number)
        if ret != -1:
            print(ret * number)
            break