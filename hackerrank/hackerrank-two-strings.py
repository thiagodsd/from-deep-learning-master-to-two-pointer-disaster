import math
import os
import random
import re
import sys


def twoStrings(s1:str, s2:str) -> str:
    hash_1 = set(s1)
    for i in s2:
        if i in hash_1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')
    fptr.close()
