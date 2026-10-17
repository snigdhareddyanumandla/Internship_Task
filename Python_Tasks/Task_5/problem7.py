# 7.symetric difference
# Hacker rank link:
https://www.hackerrank.com/challenges/symmetric-difference/problem


if __name__ == '__main__':
    m_size = int(input())
    set_m = set(map(int, input().split()))
    
    n_size = int(input())
    set_n = set(map(int, input().split()))
    
    # Compute the symmetric difference using symmetric_difference() and sort it
    sym_diff = sorted(set_m.symmetric_difference(set_n))
    
    # Print each value on a new line
    for val in sym_diff:
        print(val)
