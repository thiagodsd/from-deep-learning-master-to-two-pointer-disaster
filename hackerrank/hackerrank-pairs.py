#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# def pairs(k, arr):
#     """
#     1 5 3 4 2, k=2
#     3-1
#     5-3
#     4-2
#     """
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] > k:
#             target = arr[i] - k
#             for j in range(len(arr)):
#                 if arr[j] == target:
#                     count += 1
#     return count


# def pairs(k, arr):
#     """
#     1 5 3 4 2, k=2
#     3-1
#     5-3
#     4-2
#     """
#     count = dict()
#     for i in range(len(arr)):
#         if arr[i] > k:
#             target = arr[i] - k
#             if target in count:
#                 count[target] += 1
#             else:
#                 for j in range(len(arr)):
#                     if arr[j] == target:
#                         count[target] = 1
#     return sum(count.values())


def pairs(k, arr):
    """
    1 5 3 4 2, k=2 (a-b=k)
    3-1
    5-3
    4-2
    """
    hash_set = set(arr)
    count = 0
    for num in arr:
        if num + k in hash_set:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
