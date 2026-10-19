# 11.Two strings
# hacker rank link:
https://www.hackerrank.com/challenges/two-strings/problem


def twoStrings(s1, s2):
    # Check if the intersection of character sets is non-empty
    return "YES" if set(s1) & set(s2) else "NO"

if __name__ == '__main__':
    p = int(input())
    for _ in range(p):
        s1 = input().strip()
        s2 = input().strip()
        result = twoStrings(s1, s2)
        print(result)
