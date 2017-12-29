#Python 2

import sys


n = int(raw_input().strip())

times = 1
for i in range(1,n+1):
    printout = ""
    printout += " " * (n-times)
    printout += "#" * times
    print printout
    times += 1
