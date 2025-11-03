import math
import os
import random
import re
import sys


def arrayManipulation(n: int, queries: list) -> int:
    """
    psychological support:
        - add k between a and b (convention: index+1)
        - 1-dimensional array
        - return the maximum value
        - l[x:y] inclusive both
        - ex:
            5 3
            1 2 100
            2 5 100
            3 4 100
            [  0,   0,   0,   0, 0]
            [100, 100,   0,   0, 0]
            [100, 200, 100, 100, 100]
            [100, 200, 200, 200, 100]
            200
        - [    0,     0,      0,   0,    0, dummy]
          [  100,     0,   -100,   0,    0, dummy]
          [  100,   100,   -100,   0,    0, -100]
          [  100,   100,      0,   0, -100, -100] (result_list)
          -> [100, 200, 200, 200, 100]
    study:
        * difference array -> analogia do elevador
        * prefix sum
    """
    result_list = [0] * (n + 2)
    for arr in queries:
        a, b, k = arr
        result_list[a] += k
        result_list[b + 1] -= k
    max_element = int()
    current = int()
    for prefix_sum in result_list:
        current += prefix_sum
        max_element = max(current, max_element)
    return max_element


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + "\n")
    fptr.close()
