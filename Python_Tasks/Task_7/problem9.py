# 9.beautiful binary string
# Hacker rank link:
https://www.hackerrank.com/challenges/beautiful-binary-string/problem



def beautifulBinaryString(b):
    # Count the non-overlapping occurrences of "010"
    return b.count('010')

if __name__ == '__main__':
    n = int(input())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)
