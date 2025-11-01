#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     """
#     psychological support
#     [2 3 4 1 5]
#     i,v
#     {
#         v: (v-1,i),
#         1: (0, 3) -> {0:3}       
#         2: (1, 0) -> {1:{0:3}}
#         3: (2, 1) -> {1:{2}}
#         4: (3, 2), x
#         5: (4, 4)
#     }
#     """
#     not_check = set(arr)
#     while not_check:
#         swap_candidate = list()
#         swap_operation = list()
#         for index, value in enumerate(arr):
#             if index == (value-1):
#                 not_check.remove(value)
#             elif (index not in swap_candidate) or (value-1 not in swap_candidate):
#                 op = [index, value-1]
#                 swap_candidate.extend(op)
#                 swap_operation.append(op)
#         for index, value in swap_operation:
#             arr[index] = value+1
#             arr[value] = index+1
#     return arr
    
    
def minimumSwaps(arr:list) -> int:
    swaps = int()
    checked = [False] * len(arr)
    for i in range(len(arr)):
        if checked[i] or (i == arr[i]-1):
            continue
        count = 0
        while not checked[i]:
            current_value = arr[i]
            target_value = arr[arr[i]-1]
            correct_index = current_value-1
            arr[correct_index] = current_value
            arr[i] = target_value
            checked[correct_index] = True
            count += 1
        swaps += count-1
    return swaps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
