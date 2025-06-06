#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# 'getTotal' function gets total count of numbers that are:
#  1. Factored by all numbers in the first array, a, ie every number in 1st array can divide the number
#  2. Factors of all numbers in the second array, b, ie every number in 2nd array is divisible by the number in consideration
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    '''
    res = []
    for i in b:
        j = 1
        while j < i:
            if i % j == 0:
                res.append(j)
            j += 1
    for i in a:
        for elem in res:
            if elem % i != 0:
                res.remove(elem)

    for i in res:
        for j in res:
            if i % j != 0:
                if i in res:
                    res.remove(i)

    res = set(res)
    return len(res)
    
    # the above solution does not handle all edge cases correctly and would also not scale well with very huge arrays
    '''
    #the simple elegant  sol
    count = 0
    for num in range(max(a), min(b) + 1): #iterate through the possible min(largest val in a) and max(smallest val in b) values
        valid = True

        # find numbers in possible range that are factored by 1st list's elements
        for j in a:
            if num % j != 0:
                valid = False
                break
        if not valid:
            continue

        #find numbers in possible range that are factors of 2nd list's elements
        for i in b:
            if i % num != 0:
                valid = False
                break
        #both conditions have to be met for it to count
        if valid:
            count += 1
    return count
