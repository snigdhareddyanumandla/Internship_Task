# 8.set.add()
# hacker rank link:
https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    stamps = set()
    
    # Read each country name and add it to the set
    for _ in range(n):
        stamps.add(input().strip())
        
    # Print the total number of distinct country stamps
    print(len(stamps))
