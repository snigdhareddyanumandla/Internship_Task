# 5.string validators
# hacker rank link:
https://www.hackerrank.com/challenges/string-validators/problem


if __name__ == '__main__':
    s = input()
    
    # Check for alphanumeric characters
    print(any(c.isalnum() for c in s))
    
    # Check for alphabetical characters
    print(any(c.isalpha() for c in s))
    
    # Check for digits
    print(any(c.isdigit() for c in s))
    
    # Check for lowercase characters
    print(any(c.islower() for c in s))
    
    # Check for uppercase characters
    print(any(c.isupper() for c in s))
