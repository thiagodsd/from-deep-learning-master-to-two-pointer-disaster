import math
import os
import random
import re
import sys
from typing import Union
from collections import defaultdict


def freqQuery(queries:list) -> Union[int, list[int]]:
    """
    psychological support
        [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
    """
    output = list()
    element_frequency = defaultdict(int)
    frequency_element = defaultdict(int)
    for operation, value in queries:
        if operation == 1:
            val_freq = element_frequency[value]                   # o numero tinha freq e vai aumentar +1
            if val_freq > 0:
                frequency_element[val_freq] -= 1                  # entao aquela freq perde 1
                if frequency_element[val_freq] == 0:
                    del frequency_element[val_freq]               # se for nulo deleta
            element_frequency[value] += 1                         # o elemento aumenta de fato
            frequency_element[element_frequency[value]] += 1      # a nova frequencia dele ganha +1
        elif operation == 2:
            val_freq = element_frequency[value]
            if val_freq > 0:
                frequency_element[val_freq] -= 1
                if frequency_element[val_freq] == 0:
                    del frequency_element[val_freq]
                element_frequency[value] -= 1
                if element_frequency[value] > 0:
                    frequency_element[element_frequency[value]] += 1
        elif operation == 3:
            output.append(1 if value in frequency_element else 0)
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freqQuery(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
