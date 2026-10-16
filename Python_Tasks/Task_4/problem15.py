# 15.word order
# hacker rank link:
https://www.hackerrank.com/challenges/word-order/problem


if __name__ == '__main__':
    n = int(input())
    
    # Read all words and store them while preserving the input order
    words = []
    for _ in range(n):
        words.append(input().strip())
        
    # Use a dictionary to keep track of frequencies and insertion order (Python 3.7+)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # Output the total number of distinct words
    print(len(word_counts))
    
    # Output the number of occurrences for each distinct word in order of appearance
    print(*(word_counts.values()))
