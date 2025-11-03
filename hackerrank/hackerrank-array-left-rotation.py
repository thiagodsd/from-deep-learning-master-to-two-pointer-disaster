import math
import os
import random
import re
import sys


def rotLeft(a:list, d:int):
    """
    1 2 3 4 5
    2 3 4 5 1 
    """
    list_lenght = len(a)
    remainder = d % list_lenght
    return a[remainder:] + a[:remainder]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
