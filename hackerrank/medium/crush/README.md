# Array Manipulation

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each array element between two given indices, inclusive.  Once all operations have been performed, return the maximum value in the array.  

**Example**  
$n = 10$  
$queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]$  

Queries are interpreted as follows:  
```
    a b k
    1 5 3
    4 8 7
    6 9 1
```

Add the values of $k$ between the indices $a$ and $b$ inclusive:


![image](https://s3.amazonaws.com/hr-assets/0/1738699658-ff37fa31d8-array_manipulation_example.png)

The largest value is $10$ after all operations are performed.  

**Function Description**  

Complete the function $arrayManipulation$ with the following parameters:

- $int\ n$: the number of elements in the array  
- $int\ queries[q][3]$: a two dimensional array of queries where each $queries[i]$ contains three integers, $a$, $b$, and $k$.  

**Returns**  

- $int$: the maximum value in the resultant array  

**Input Format**

The first line contains two space-separated integers $n$ and $q$, the size of the array and the number of queries.  
Each of the next $q$ lines contains three space-separated integers $a$, $b$ and $k$, the left index, right index and number to add.  

**Constraints**

- $3 \le n \le 10^{7}$  
- $1 \le m \le 2 * 10^{5} $  
- $1 \le a \le b \le n   $  
- $0 \le k \le 10^{9}  $  


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T19:39:58.923Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    diff = [0] * (n + 2)
    for a, b, k in queries:
        diff[a] += k
        diff[b + 1] -= k

    current = 0
    maximum = 0

    for i in range(1, n + 1):
        current += diff[i]
        maximum = max(maximum, current)

    return maximum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/crush/problem)