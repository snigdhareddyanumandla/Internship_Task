# 12.capitalize
# Hacker rank link:
https://www.hackerrank.com/challenges/capitalize/problem



def solve(s):
    # Split the string by spaces to preserve exact spacing, 
    # capitalize each word, and join them back together
    return ' '.join(word.capitalize() for word in s.split(' '))
