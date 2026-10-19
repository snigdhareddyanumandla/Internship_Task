# 19.company logo
# Hacker rank link:
https://www.hackerrank.com/challenges/most-commons/problem



from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # Count character occurrences and sort by count descending, then alphabetically ascending
    counted = Counter(s)
    sorted_chars = sorted(counted.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 most common characters with their occurrence counts
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
