
import sys

def solve(grades):
    # Complete this function
    roundedGrades = []
    for grade in grades:
        if grade < 38:
            roundedGrades.append(grade)
        elif (grade % 5) > 2:
            roundedG = grade+(5-(grade%5))
            roundedGrades.append(roundedG)
        else:
            roundedGrades.append(grade)
    return roundedGrades        
            
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
