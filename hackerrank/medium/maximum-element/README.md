# Maximum Element

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You have an empty sequence, and you will be given $N$ queries. Each query is one of these three types:

	1 x  -Push the element x into the stack.
    2    -Delete the element present at the top of the stack.
    3    -Print the maximum element in the stack.

**Function Description**  

Complete the *getMax* function in the editor below.   

*getMax* has the following parameters:  
- *string operations[n]:* operations as strings   

**Returns**  
- *int[]:* the answers to each type 3 query   

**Input Format**

The first line of input contains an integer, $n$. The next $n$ lines each contain an above mentioned query.   



**Constraints**

 **Constraints**  
$1 \le n \le 10^5$  
$1 \le x \le 10^9$  
$1 \le type \le 3$   
All queries are valid.  



**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T19:59:43.993Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/maximum-element/problem)