# 15.Game of Thrones - I
# hacker rank link:
https://www.hackerrank.com/challenges/game-of-thrones/problem




from collections import Counter

def gameOfThrones(s):
    # Count the frequency of each character in the string
    char_counts = Counter(s)
    
    # Count how many characters have an odd frequency
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # A string can be rearranged into a palindrome if:
    # 1. Total length is even and 0 characters have an odd count, OR
    # 2. Total length is odd and exactly 1 character has an odd count
    if len(s) % 2 == 0:
        return "YES" if odd_count == 0 else "NO"
    else:
        return "YES" if odd_count == 1 else "NO"

if __name__ == '__main__':
    s = input().strip()
    result = gameOfThrones(s)
    print(result)
