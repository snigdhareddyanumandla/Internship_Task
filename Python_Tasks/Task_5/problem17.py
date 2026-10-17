# 17.No ideal
# hacker rank link:
https://www.hackerrank.com/challenges/no-idea/problem



if __name__ == '__main__':
    # Read n and m
    n, m = map(int, input().split())
    
    # Read the array of integers
    arr = list(map(int, input().split()))
    
    # Read sets A and B, converted to sets for O(1) lookup time
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    # Calculate the total happiness using a generator expression and sum()
    happiness = sum((i in set_a) - (i in set_b) for i in arr)
    
    # Output the final happiness
    print(happiness)
