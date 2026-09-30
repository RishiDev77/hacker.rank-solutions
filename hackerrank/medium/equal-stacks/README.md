# Equal Stacks

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times. 

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.  

**Example**  

$h1 = [1, 2, 1, 1]$  
$h2 = [1, 1, 2]$  
$h3 = [1, 1]$  

There are $4, 3$ and $2$ cylinders in the three stacks, with their heights in the three arrays.  Remove the top 2 cylinders from $h1$ (heights = [1, 2]) and from $h2$ (heights = [1, 1]) so that the three stacks all are 2 units tall.  Return $2$ as the answer.  

**Note:** An empty stack is still a stack.  

**Function Description**  

Complete the _equalStacks_ function in the editor below.

_equalStacks_ has the following parameters:  

- *int h1[n1]:* the first array of heights  
- *int h2[n2]:* the second array of heights  
- *int h3[n3]:* the third array of heights  

**Returns**  

- *int:* the height of the stacks when they are equalized  

**Input Format**

The first line contains three space-separated integers, $n1$, $n2$, and $n3$, the numbers of cylinders in stacks $1$, $2$, and $3$. The subsequent lines describe the respective heights of each cylinder in a stack *from top to bottom*:		

- The second line contains $n1$ space-separated integers, the cylinder heights in stack $1$. The first element is the top cylinder of the stack.  
- The third line contains $n2$ space-separated integers, the cylinder heights in stack $2$. The first element is the top cylinder of the stack.  	
- The fourth line contains $n3$ space-separated integers, the cylinder heights in stack $3$.	The first element is the top cylinder of the stack.  

**Constraints**

* $0 < n1, n2, n3 \le 10^5$
* $0 < \textit{ height of any cylinder } \le 100$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T20:03:27.642Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    i = 0
    j = 0
    k = 0

    while not (sum1 == sum2 == sum3):

        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1[i]
            i += 1

        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2[j]
            j += 1

        else:
            sum3 -= h3[k]
            k += 1

    return sum1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/equal-stacks/problem)