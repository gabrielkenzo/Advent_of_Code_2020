import os
import sys
from ex1 import tree_counter

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "input.txt"))
    lines = file.read().splitlines()
    file.close()
    
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for (a, b) in slopes:
        result *= tree_counter(a, b, lines) 
    print(result)