#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'partitionArray' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY numbers
#

def partitionArray(k, numbers):
    for i in range(k):
        if numbers[i] != numbers[i + 1]:
            print("Yes")
        else:
            print("No")
        i += i

if __name__ == '__main__':
    fptr = sys.stdout
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input("Value of k: ").strip())

    numbers_count = int(input("Number count: ").strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input("Hi ").strip())
        numbers.append(numbers_item)

    result = partitionArray(k, numbers)

    fptr.write(result + '\n')

    fptr.close()
