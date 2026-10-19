# 10.camelcase
# Hacker rank link:
https://www.hackerrank.com/challenges/camelcase/problem


def camelcase(s):
    # Count uppercase letters and add 1 for the first word
    return sum(1 for c in s if c.isupper()) + 1

if __name__ == '__main__':
    s = input().strip()
    result = camelcase(s)
    print(result)
