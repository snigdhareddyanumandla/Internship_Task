# set.add()
# hacker rank link:
https://www.hackerrank.com/challenges/py-set-add/problem
if __name__ == '__main__':
    N = int(input())
    
    # Initialize an empty set to store unique country stamps
    stamps = set()
    
    # Read each country name and add it to the set
    for _ in range(N):
        stamps.add(input())
        
    # Print the total number of distinct country stamps
    print(len(stamps))
