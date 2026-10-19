# 5.Alternating charachters
# Hacker rank link:
https://www.hackerrank.com/challenges/alternating-characters/problem


def alternatingCharacters(s):
    # Count consecutive matching characters to find minimum deletions
    return sum(1 for i in range(len(s) - 1) if s[i] == s[i+1])

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(alternatingCharacters(s))
