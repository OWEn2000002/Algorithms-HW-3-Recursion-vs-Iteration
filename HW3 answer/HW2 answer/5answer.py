#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Read numbers from file
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

# Merge Sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Binary search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid  # Element found
    return -1  # Element not found

# Main program
file_name = 'numbers-3.txt'
numbers = read_numbers_from_file(file_name)

# Sort the numbers
merge_sort(numbers)

# Perform binary search for specific numbers
number_1_position = binary_search(numbers, 8128705)
number_2_position = binary_search(numbers, 5842193)

print(f"Position of 8128705: {number_1_position}")
print(f"Position of 5842193: {number_2_position}")
