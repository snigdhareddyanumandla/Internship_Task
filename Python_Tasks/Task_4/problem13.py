# 13.symmetric difference
# hacker rank link:
https://www.hackerrank.com/challenges/symmetric-difference/problem
if __name__ == '__main__':
    M = int(input())
    set_m = set(map(int, input().split()))
    N = int(input())
    set_n = set(map(int, input().split()))
    
    # Find the symmetric difference and sort the values in ascending order
    sym_diff = sorted(set_m.symmetric_difference(set_n))
    
    # Print each value on a separate line
    for val in sym_diff:
        print(val)
