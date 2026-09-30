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
