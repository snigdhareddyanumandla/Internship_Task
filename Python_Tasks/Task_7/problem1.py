#1.Set .symmetric_difference() Operation
# Hacker rank link:
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    
    # Find the symmetric difference to get students subscribed to either English or French, but not both
    symmetric_diff = english_set.symmetric_difference(french_set)
    print(len(symmetric_diff))
