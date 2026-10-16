# 12.introduction to sets
# hacker rank link:
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # Convert the array to a set to remove duplicate heights
    distinct_heights = set(array)
    
    # Calculate the average by dividing the sum of distinct heights by their count
    avg = sum(distinct_heights) / len(distinct_heights)
    
    return avg
