# 14.Anagram
# Hacker rank link:
https://www.hackerrank.com/challenges/anagram/problem



from collections import Counter

def anagram(s):
    # If the length of the string is odd, it cannot be split into two equal halves
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Count character frequencies for both halves
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Subtracting counts leaves the characters in s1 that need to be changed
    diff = count1 - count2
    
    # Summing the values gives the minimum number of changes required
    return sum(diff.values())

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        result = anagram(s)
        print(result)
