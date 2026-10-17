# 1.Find the Runner-up score!
# hacker rank link:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Remove duplicate scores using a set and sort them in ascending order
    unique_scores = sorted(list(set(arr)))
    
    # The runner-up score is the second-to-last element in the sorted unique list
    print(unique_scores[-2])
