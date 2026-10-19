# 13.Set .union() Operation
# Hacker rank link:
https://www.hackerrank.com/challenges/py-set-union/problem



if __name__ == '__main__':
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    
    # Find the union of both sets to get students subscribed to at least one newspaper
    total_students = english_set.union(french_set)
    print(len(total_students))
