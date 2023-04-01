import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    unsorted_value =arr[-1]
    
    for index in range(n-2, -1, -1):
        if arr[index]>unsorted_value:
            arr[index+1] =arr[index]
            print(*arr)
        else:
            arr[index+1]= unsorted_value
            print(*arr)
           

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
