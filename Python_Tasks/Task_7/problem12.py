# 12.making anagrams
# Hacker rank link:
https://www.hackerrank.com/challenges/making-anagrams/problem


from collections import Counter

def makingAnagrams(s1, s2):
    # Count character frequencies for both strings
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Subtracting counts leaves the absolute difference in frequencies
    diff = count1 - count2 + (count2 - count1)
    
    # Return the sum of all character frequency differences
    return sum(diff.values())

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    result = makingAnagrams(s1, s2)
    print(result)
