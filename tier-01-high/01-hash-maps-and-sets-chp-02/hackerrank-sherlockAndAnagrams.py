#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import defaultdict

def sherlockAndAnagrams(string:str) -> int:
    count = defaultdict(int)
    # pensando na substring primeiro porque o problema dos pares e um corolario
    for char_index in range(len(string)):
        for substring_char_index in range(char_index+1, len(string)+1):
            substring = string[char_index:substring_char_index]
            signature = ''.join(sorted(substring))
            count[signature] += 1
    final_result = 0
    for freq in count.values():
        final_result += freq * (freq-1)//2 # aqui fodeu porque tem que lembrar que c(n,k) = n!/k!(n-k)!
    return final_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
