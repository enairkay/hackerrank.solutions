#Completed in Python 2

import sys


N = int(raw_input().strip())
if N%2 != 0:
    print "Weird"
else:
    if N < 6 and N > 1:
        print "Not Weird"
    elif (N > 5 and N < 21):
        print "Weird"
    elif N >= 21:
        print "Not Weird"

