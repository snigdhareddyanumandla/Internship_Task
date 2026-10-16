# 5.Print Function
# hacker rank link:
https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    
    # Loop from 1 to n and print each integer on the same line without spaces
    for i in range(1, n + 1):
        print(i, end='')
