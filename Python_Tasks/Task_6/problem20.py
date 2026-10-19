# 20.Validating the Phone Number
# Hacker rank link:
https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com




import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        number = input().strip()
        # Check if the number is a 10-digit number starting with 7, 8, or 9
        if re.match(r'^[789]\d{9}$', number):
            print("YES")
        else:
            print("NO")
