# 10.Designer Door mat
# Hacker rank link:
https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    # Top pattern
    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))
        
    # Center line
    print('WELCOME'.center(m, '-'))
    
    # Bottom pattern
    for i in range(n - 2, 0, -2):
        print(('.|.' * i).center(m, '-'))
