import math
import os
import random
import re
import sys


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
