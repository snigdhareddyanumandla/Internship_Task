# 6.Introduction to sets
# hacker rak link:
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(arr):
    # Convert the array to a set to filter out duplicate heights
    distinct_heights = set(arr)
    
    # Calculate the average using the sum and total number of distinct heights
    avg = sum(distinct_heights) / len(distinct_heights)
    
    # Return the result rounded to 3 decimal places
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
