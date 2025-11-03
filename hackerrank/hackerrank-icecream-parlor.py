import math
import os
import random
import re
import sys


def icecreamParlor(m: int, arr: list) -> list:
    already_seen = dict()
    for index, cost in enumerate(arr):
        complement = m - cost
        if complement in already_seen:
            return [already_seen[complement] + 1, index + 1]
        already_seen[cost] = index
    return list()


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")  # anwser
    t = int(input().strip())  # number of trips
    for t_itr in range(t):
        m = int(input().strip())  # target budget
        n = int(input().strip())  # number of flavors offered
        arr = list(map(int, input().rstrip().split()))  # cost of each flavor
        result = icecreamParlor(m, arr)
        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")
    fptr.close()
