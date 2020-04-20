#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    amOrPm = s[-2:]
    li = s.split(":")
    num = int(li[0])
    if amOrPm == "PM":
        if num < 12:
            num += 12
            return str(num) + s[2:-2]
        else:
            return str(num) + s[2:-2]
    else:
        if num == 12:
            return "00" + s[2:-2] 
        else:
            return "0" + str(num) + s[2:-2]
        
   
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
