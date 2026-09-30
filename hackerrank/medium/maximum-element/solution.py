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
    stack = []
    max_stack = []
    result = []

    for operation in operations:
        parts = operation.split()

        if parts[0] == "1":
            x = int(parts[1])
            stack.append(x)

            if not max_stack:
                max_stack.append(x)
            else:
                max_stack.append(max(x, max_stack[-1]))

        elif parts[0] == "2":
            stack.pop()
            max_stack.pop()

        elif parts[0] == "3":
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
