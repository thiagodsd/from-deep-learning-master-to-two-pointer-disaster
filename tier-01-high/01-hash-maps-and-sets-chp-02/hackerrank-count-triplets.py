#!/bin/python3

import math
import os
import random
import re
import sys

# # Complete the countTriplets function below.
# def countTriplets(arr:list, r:int) -> int:
#     triplets = set()
#     for i in range(len(arr)-2):
#         for j in range(i+1, len(arr)-1):
#             for k in range(j+1, len(arr)):
#                 if (arr[i]*r == arr[j]) and (arr[j]*r == arr[k]):
#                     triplets.add((i,j,k))
#     return len(triplets)

# def countTriplets(arr: list, r: int) -> int:
#     pairs = dict()
#     triplets = dict()
#     count = 0
#     for num in arr:
#         count += pairs.get(num, 0)
#         pairs[num*r] = pairs.get(num*r,0) + triplets.get(num,0)
#         triplets[num*r] = triplets.get(num*r,0) + 1
#     return count

from collections import defaultdict

# exemplo
# (1,3,9,9,27,81), r=3
# dado um numero eu devo me perguntar
# (1) alguma candidata a tripla estava esperando esse numero? ---> triplet[num]?
# (2) alguma candidata a dupla pode ser convertida em candidata a tripla? ---> pairs[num]
# (3) o numero pode iniciar um candidato a dupla sempre
#
# num=1 ---> count+=triplet[1]=0 | triplet[1x3=3]+=pairs[1]=0 | pairs[1x3=3]+=1
# num=3 ---> count+=triplet[3]=0 | triplet[3x3=9]+=pairs[3]=1 | pairs[3x3=9]+=1
# num=9 ---> count+=triplet[9]=1 | triplet[9x3=27]+=pairs[9]=1 | pairs[9x3=27]+=1
# num=9 ---> count+=triplet[9]=1 | triplet[9x3=27]+=pairs[9]=1 | pairs[9x3=27]+=1
def countTriplets(arr: list, r: int) -> int:
    pairs = defaultdict(int) # avoids .get(,0)
    triplets = defaultdict(int)
    count = 0
    for num in arr:
        count += triplets[num] # match com dupla candidata a tripla 
        triplets[num*r] += pairs[num] # o par que foi formado virou candidato a tripla
        pairs[num*r] += 1 # aparece mais um candidato a par
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()
