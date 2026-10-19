# 18.String Construction
# hacker rank link:
https://www.hackerrank.com/challenges/string-construction/problem



def stringConstruction(s):
    # The minimum cost equals the number of unique characters in the string
    return len(set(s))

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
