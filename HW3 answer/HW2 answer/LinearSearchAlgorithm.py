#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# 1、 Iterative Linear Search Algorithm in Python
def iterative_linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index if match found
    return -1  # Return -1 if element not found

# 2、 Recursive Linear Search Algorithm in Python
def recursive_linear_search(arr, x, start=0):
    if start >= len(arr):
        return -1  # Base case: element not found
    if arr[start] == x:
        return start  # Base case: return index if match found
    else:
        return recursive_linear_search(arr, x, start+1)  # Recursively search from the next index


# Test the algorithms result:
arr = [7, 1, 6, 3, 5, 2, 8, 9, 4]
x = 5

print(iterative_linear_search(arr, x))  # Output: 4 (index of the element)
print(recursive_linear_search(arr, x))  # Output: 4 (index of the element)