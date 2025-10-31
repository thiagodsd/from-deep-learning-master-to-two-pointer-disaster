#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine:list, note:list) -> str:
    magazine_freq = dict()
    for word in magazine:
        if word in magazine_freq:
            magazine_freq[word] += 1
        else:
            magazine_freq[word] = 1
    for word in note:
        if (word in magazine_freq) and (magazine_freq[word] > 0):
           magazine_freq[word] -= 1
        else:
            return "No"
    return "Yes"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    print(checkMagazine(magazine, note))
