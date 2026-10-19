# 13.Sherlock and the Valid String
# Hacker rank link:
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem



from collections import Counter

def isValid(s):
    # Count the frequency of each character in the string
    char_counts = Counter(s)
    # Count how many times each frequency value occurs
    freq_counts = Counter(char_counts.values())
    
    # Case 1: All characters already have the exact same frequency
    if len(freq_counts) == 1:
        return "YES"
    
    # Case 2: There are two distinct frequency values
    if len(freq_counts) == 2:
        f1, f2 = sorted(freq_counts.keys())
        # Sub-case A: The lower frequency is 1 and it occurs only once (we can remove that single character)
        if f1 == 1 and freq_counts[f1] == 1:
            return "YES"
        # Sub-case B: The higher frequency is greater than the lower by 1, and it occurs only once (we can reduce it by 1)
        if f2 - f1 == 1 and freq_counts[f2] == 1:
            return "YES"
            
    # Otherwise, it cannot be made valid by removing just 1 character
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    result = isValid(s)
    print(result)
