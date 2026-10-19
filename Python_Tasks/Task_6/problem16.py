# 16.Check subset
# Hacker rank link:
https://www.hackerrank.com/challenges/py-check-subset/problem


if __name__ == '__main__':
    for _ in range(int(input())):
        n_a = int(input())
        set_a = set(map(int, input().split()))
        n_b = int(input())
        set_b = set(map(int, input().split()))
        
        # Check if set A is a subset of set B
        print(set_a.issubset(set_b))
