import math
import os
import random
import re
import sys


def makeAnagram(a, b):
    """
    psychological support
        cdeee -> {c:1, d:1, e:3}       -> d:1, e:2
        abbce -> {a:1, b:2, c:1, e:1}  -> a:1, b:2, e:2
    """
    result = int()
    differences = dict()
    
    def counter(arr:list) -> dict:
        result = dict()
        for i in arr:
            result[i] = result.get(i, 0) + 1
        return result
    
    count_a = counter(a)
    count_b = counter(b)
    
    for key in count_a:
        differences[key] = max(
            differences.get(key, 0),
            count_a[key] - count_b.get(key, 0)
        )
    
    for key in count_b:
        differences[key] = max(
            differences.get(key, 0),
            count_b[key] - count_a.get(key, 0)
        )
    
    for key in differences:
        result += differences[key]
        
    return result
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
