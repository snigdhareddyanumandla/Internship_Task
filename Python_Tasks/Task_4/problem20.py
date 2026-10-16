#20.no-ideal!
# hacker rank link:
https://www.hackerrank.com/challenges/no-idea/problem


if __name__ == '__main__':
    # Read n and m
    n, m = map(int, input().split())
    
    # Read the array of n integers
    array = list(map(int, input().split()))
    
    # Read sets A and B
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    # Calculate happiness using a generator expression and set membership
    happiness = sum((1 if i in set_a else -1 if i in set_b else 0) for i in array)
    
    # Print the total happiness
    print(happiness)
