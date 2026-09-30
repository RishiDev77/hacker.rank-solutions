# Queue using Two Stacks

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a *First-In-First-Out* (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

- *Enqueue*: add a new element to the end of the queue.
- *Dequeue*: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using *two stacks*. Then process $q$ queries, where each query is one of the following $3$ types: 

1. `1 x`: Enqueue element $x$ into the end of the queue.
2. `2`: Dequeue the element at the front of the queue.
3. `3`: Print the element at the front of the queue.



**Input Format**

The first line contains a single integer, $q$, denoting the number of queries. 	
Each line $i$ of the $q$ subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query $type$, but only query $1$ is followed by an additional space-separated value, $x$, denoting the value to be enqueued.

**Constraints**

- $1 \le q \le 10^5$  
- $1 \le type \le 3$  
- $1 \le |x| \le 10^9$  
- It is guaranteed that a valid answer always exists for each query of type $3$.


**Output Format**

For each query of type $3$, print the value of the element at the front of the queue on a new line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T20:05:43.530Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    q = int(input())

    stack1 = []
    stack2 = []

    for _ in range(q):
        query = input().split()

        if query[0] == '1':
            x = int(query[1])
            stack1.append(x)

        elif query[0] == '2':
            if not stack2:
                while stack1:
                    stack2.append(stack1.pop())

            stack2.pop()

        elif query[0] == '3':
            if not stack2:
                while stack1:
                    stack2.append(stack1.pop())

            print(stack2[-1])

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/queue-using-two-stacks/problem)