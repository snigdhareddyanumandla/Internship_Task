# 11.text wrap
# Hacker rank link:
https://www.hackerrank.com/challenges/text-wrap/problem


import textwrap

def wrap(string, max_width):
    # textwrap.fill automatically wraps the string into a paragraph of the specified max width
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
