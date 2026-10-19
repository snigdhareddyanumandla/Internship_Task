# 15.Set .difference() Operation
# Hacker rank link:
https://www.hackerrank.com/challenges/py-set-difference-operation/problem


if __name__ == '__main__':
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    
    # Find the difference to get students subscribed only to the English newspaper
    only_english = english_set.difference(french_set)
    print(len(only_english))
