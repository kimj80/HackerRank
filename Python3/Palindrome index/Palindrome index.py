#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    start = 0
    end = len(s) - 1
    wordLen = len(s)

    if s == s[::-1]:
        return -1

    while start < end:
        if s[start] != s[end]:
            front = s[start:end]
            back = s[start + 1:end + 1]
            if front == front[::-1]:
                return end
            elif back == back[::-1]:
                return start

        start += 1
        end -= 1

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
