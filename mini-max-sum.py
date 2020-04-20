#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = 0
    for i in arr:
        total += i
    maxi = max(arr)
    mini = min(arr)
    print(total-maxi, total-mini)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
