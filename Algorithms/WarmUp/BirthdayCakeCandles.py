#Python 2

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    maxHeight = max(ar)
    return ar.count(maxHeight)
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
