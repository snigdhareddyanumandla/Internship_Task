# 8.gemstones
# Hacker rank link:
https://www.hackerrank.com/challenges/gem-stones/problem


def gemstones(arr):
    # Find the intersection of character sets for all rocks in the array
    common_minerals = set(arr[0])
    for rock in arr[1:]:
        common_minerals.intersection_update(set(rock))
        
    return len(common_minerals)

if __name__ == '__main__':
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    result = gemstones(arr)
    print(result)
