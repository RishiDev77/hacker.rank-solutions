# String Formatting

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer, $n$, print the following values for each integer $i$ from $1$ to $n$:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

**Function Description**   

Complete the *print_formatted* function in the editor below.   

*print_formatted* has the following parameters:   

-	*int number:* the maximum value to print  

**Prints**   

The four values must be printed on a single line *in the order specified above* for each $i$ from $1$ to $number$. Each value should be space-padded to match the width of the *binary* value of $number$ and the values should be separated by a single space.

**Input Format**

A single integer denoting $n$.

**Constraints**

- $1 \le n \le 99$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T19:31:09.242Z  

```py
def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(str(i).rjust(width),
              oct(i)[2:].rjust(width),
              hex(i)[2:].upper().rjust(width),
              bin(i)[2:].rjust(width))



```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-string-formatting/problem)