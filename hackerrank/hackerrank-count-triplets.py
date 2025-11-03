import math
import os
import random
import re
import sys


def triplets(a:list, b:list, c:list) -> int:
    """
    psychological support
        p \in a
        q \in b
        r \in c
            p <= q
            r <= q
        ---
        a = [1, 3, 5] 
        b = [2, 3]
        c = [1, 2, 3]
    """
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    result = int()
    
    def binary_search(arr:list, target:int) -> int:
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    for q in b:
        count_a = binary_search(a, q)
        count_c = binary_search(c, q)
        result += count_a * count_c
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    fptr.write(str(ans) + '\n')
    fptr.close()
