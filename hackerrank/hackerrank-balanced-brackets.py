import math
import os
import random
import re
import sys


def isBalanced(s: str) -> str:
    """
    psychological support:
        - {[(])}
    """
    stack = list()
    brackets = {"]": "[", ")": "(", "}": "{"}
    for char in s:
        if char in brackets:
            if (not stack) or (stack[-1] != brackets[char]):
                return "NO"
            else:
                stack.pop()
        else:
            stack.append(char)
    return "YES" if (not stack) else "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + "\n")
    fptr.close()
