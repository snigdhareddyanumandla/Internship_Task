# 9.word order
# Hacker rank link:
https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    word_counts = OrderedDict()
    
    # Read each word and update its frequency in the Ordered Dictionary
    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # On the first line, output the number of distinct words
    print(len(word_counts))
    
    # On the second line, output the number of occurrences for each distinct word
    print(*(word_counts.values()))
