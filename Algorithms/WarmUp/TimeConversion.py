#Python 2

import sys

def timeConversion(s):
    # Complete this function
    dayInd = s[-2:]
    if (dayInd == "PM" and int(s[:2]) != 12):
        mainTime = s[2:-2]
        hours = str(int(s[:2])+12)
        return hours + mainTime
    elif (dayInd == "AM" and int(s[:2]) == 12):
        mainTime = s[2:-2]
        hours = "0" + str(int(s[:2])-12)
        return hours + mainTime
    else:
        return s[:-2]
        
    
s = raw_input().strip()
result = timeConversion(s)
print(result)

