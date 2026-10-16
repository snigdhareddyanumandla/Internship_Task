# 6.Find the Runner-Up Score!
# hacker rank link:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Remove duplicate scores and sort them in ascending order
    unique_scores = sorted(set(arr))
    
    # Print the second-highest score (the runner-up)
    print(unique_scores[-2])
