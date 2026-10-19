# 19.Weighted uniform strings
# Hacker rank link:
https://www.hackerrank.com/challenges/weighted-uniform-string/problem



def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    length = 0
    
    # Calculate the weights of all possible uniform contiguous substrings
    for char in s:
        weight = ord(char) - ord('a') + 1
        if char == prev:
            length += 1
        else:
            prev = char
            length = 1
        weights.add(weight * length)
        
    # Check each query against the precomputed set of weights
    result = []
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")
            
    return result

if __name__ == '__main__':
    s = input().strip()
    n = int(input())
    queries = [int(input().strip()) for _ in range(n)]
    
    answer = weightedUniformStrings(s, queries)
    print('\n'.join(answer))
