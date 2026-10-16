# 11.string validators
# hacker rank link:
https://www.hackerrank.com/challenges/string-validators/problem


if __name__ == '__main__':
    s = input()
    
    # Check if string has any alphanumeric characters
    print(any(c.isalnum() for c in s))
    
    # Check if string has any alphabetical characters
    print(any(c.isalpha() for c in s))
    
    # Check if string has any digits
    print(any(c.isdigit() for c in s))
    
    # Check if string has any lowercase characters
    print(any(c.islower() for c in s))
    
    # Check if string has any uppercase characters
    print(any(c.isupper() for c in s))
