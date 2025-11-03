import math
import os
import random
import re
import sys


def matchingStrings(stringList, queries):
    """
    psychological support:
        ['aba', 'baba', 'aba', 'xzxb']
        ['aba', 'xzxb', 'ab']
    """
    count = list()
    count_dict = dict()
    for key in stringList:
        count_dict[key] = count_dict.get(key, 0) + 1
    for q in queries:
        count.append(count_dict.get(q, 0))
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    stringList_count = int(input().strip())
    stringList = []
    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res = matchingStrings(stringList, queries)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
