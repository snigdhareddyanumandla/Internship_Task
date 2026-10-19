# 6.programs
# Hacker rank link:
https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    # Convert string to lowercase and find all unique alphabetic characters
    alphabet_set = set(c for c in s.lower() if c.isalpha())
    
    # Check if we have all 26 letters of the English alphabet
    if len(alphabet_set) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
