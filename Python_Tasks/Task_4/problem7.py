# 7.String Split and Join
# hacker rank link:
https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # Split the string on space delimiter and join with a hyphen
    return "-".join(line.split(" "))
    
