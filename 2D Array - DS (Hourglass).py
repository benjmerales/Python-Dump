#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    i,j = 1,1
    hourglasssum = []
    for _ in arr:
        print(_)

    while i <= 4:
        j = 1
        while j <= 4:
            hourglasssum.append( arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]+ arr[i][j]+ arr[i+1][j-1]+ arr[i+1][j]+ arr[i+1][j+1]) 
            j+=1
        i+=1
    print(max(hourglasssum))
    
if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    hourglassSum(arr)
