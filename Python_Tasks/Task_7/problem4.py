# 4.funny string
# Hacker rank link:
https://www.hackerrank.com/challenges/funny-string/problem


def funnyString(s):
    rev_s = s[::-1]
    
    diffs = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    rev_diffs = [abs(ord(rev_s[i]) - ord(rev_s[i-1])) for i in range(1, len(rev_s))]
    
    return "Funny" if diffs == rev_diffs else "Not Funny"

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(funnyString(s))
