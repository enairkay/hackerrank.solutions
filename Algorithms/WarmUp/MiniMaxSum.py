#Python 2


import sys

arr = map(int, raw_input().strip().split(' '))

smallest = min(arr)
largest = max(arr)
outPut = sum(arr)

print "%d %d" % (outPut-largest, outPut-smallest)
             
