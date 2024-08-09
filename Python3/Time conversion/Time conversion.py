#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours = int(s[0:2])

    if s[8] == "P":
        if hours < 12:
            hours += 12

    else:
        if hours == 12:
            hours = "00"
        elif hours < 10:
            hours = "0" + str(hours)

    time = str(hours) + s[2:-2]

    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
