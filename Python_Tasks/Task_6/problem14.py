# 14.Set .intersection() Operation
# Hacker rank link:
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


if __name__ == '__main__':
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    
    # Find the intersection of both sets to get students subscribed to both newspapers
    both_students = english_set.intersection(french_set)
    print(len(both_students))
