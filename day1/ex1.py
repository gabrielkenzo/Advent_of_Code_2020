import os
import sys

def find_complement(lines, added):
    for number in lines:
        if added - number in lines:
            return number * (added - number)
    return -1

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "input.txt"))
    lines = []
    for line in file:
        lines.append(int(line))
    file.close()
    
    print(find_complement(lines, 2020))