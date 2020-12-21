import os
import sys

def tree_counter(right, down, lines):
    count = 0
    j = 0
    line_lenght = len(lines[0])
    for i in range(down, len(lines), down):
        j = (j + right) % line_lenght
        if lines[i][j] == "#":
            count += 1
    return count

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "input.txt"))
    lines = file.read().splitlines()
    file.close()
    
    print(tree_counter(3, 1, lines))