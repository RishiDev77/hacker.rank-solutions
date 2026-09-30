# Arrays - DS

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

An *array* is a data structure that stores elements of the same type in a contiguous block of memory. In an array, $A$, of size $N$, each memory location has some unique index, $i$ (where $0 \le i \lt N$), that can be referenced as $A[i]$ or $A_i$.
    
Your task is to reverse an array of integers.   

**Note:** If you've already solved our C++ domain's *Arrays Introduction* challenge, you may want to skip this.

**Example**  
$A = [1, 2, 3]$  

Return $[3, 2, 1]$.  

**Function Description**  

Complete the function $reverseArray$ with the following parameter(s):  

- $int\ A[n]$: the array to reverse  

**Returns**  

- $int[n]$: the reversed array

**Input Format**

The first line contains an integer, $N$, the number of integers in $A$. 	
The second line contains $N$ space-separated integers that make up $A$.

**Constraints**

- $1 \le N \le 10^3$
- $1 \le A[i] \le 10^4 \text{, where } A[i] \text{ is the } i^{th} \text{ integer in } A$



**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T19:36:47.443Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/arrays-ds/problem)