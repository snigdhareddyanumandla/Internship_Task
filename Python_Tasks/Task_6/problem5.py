# 5.
# Hacker rank link:
https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    
    # Check if the year is divisible by 4 and not 100, or if it is divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        
    return leap
    
year = int(input())
print(is_leap(year))
