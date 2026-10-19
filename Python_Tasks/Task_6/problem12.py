# 12.Set .discard(), .remove() & .pop()
# Hacker rank link:
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem



if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    
    for _ in range(N):
        parts = input().split()
        command = parts[0]
        
        if command == 'pop':
            s.pop()
        elif command == 'remove':
            s.remove(int(parts[1]))
        elif command == 'discard':
            s.discard(int(parts[1]))
            
    print(sum(s))
