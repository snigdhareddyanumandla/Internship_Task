# 7.Alphabet rangoli
# Hacker rank link:
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        current_chars = alpha[i:size]
        row = "-".join(list(reversed(current_chars)) + list(current_chars[1:]))
        width = 4 * size - 3
        lines.append(row.center(width, '-'))
        
    print ('\n'.join(lines[::-1] + lines[1:]))
