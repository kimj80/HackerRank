#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary = bin(n)[2:]
    flippedBinary = ""

    if len(binary) < 32:
        for padZero in range(32 - len(binary)):
            binary = "0" + binary

    for num in binary:
        if num == "1":
            flippedBinary = flippedBinary + "0"
        else:
            flippedBinary = flippedBinary + "1"

    return int(flippedBinary, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
