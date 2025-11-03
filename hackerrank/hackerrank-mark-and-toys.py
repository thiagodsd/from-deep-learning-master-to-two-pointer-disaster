import math
import os
import random
import re
import sys


def maximumToys(prices, k):
    budget = k
    gifts = 0
    prices = sorted(prices)
    for p in  prices:
        if p <= budget:
            gifts += 1
            budget -= p
    return gifts
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
