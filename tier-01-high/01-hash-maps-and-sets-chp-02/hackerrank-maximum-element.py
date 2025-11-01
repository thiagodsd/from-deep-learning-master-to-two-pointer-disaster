#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    """
    [0, 0, 1, 1, 2, 3, 1, 0, 1, 5']
    [0, 0, 1, 1, 2, 3', 1, 0, 1]
    [0, 0, 1, 1']
    """
    stack = list()
    max_stack = list()
    result = list()
    for op in operations:
        op_type, *val = op.split()
        if op_type == '1':
            candidate = int(val[0])
            stack.append(candidate)
            if not max_stack:
                max_stack.append(candidate)
            else:
                max_stack.append(max(candidate, max_stack[-1]))
        elif op_type == '2':
            stack.pop()
            max_stack.pop()
        elif op_type == '3':
            result.append(max_stack[-1])
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ops = []
    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)
    res = getMax(ops)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
