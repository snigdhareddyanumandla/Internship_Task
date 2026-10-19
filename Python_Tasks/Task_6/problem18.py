# 18.set mutations
# Hacker rank link:
https://www.hackerrank.com/challenges/py-set-mutations/problem


if __name__ == '__main__':
    n_a = int(input())
    set_a = set(map(int, input().split()))
    n = int(input())
    
    for _ in range(n):
        op, length = input().split()
        other_set = set(map(int, input().split()))
        
        if op == 'intersection_update':
            set_a.intersection_update(other_set)
        elif op == 'update':
            set_a.update(other_set)
        elif op == 'symmetric_difference_update':
            set_a.symmetric_difference_update(other_set)
        elif op == 'difference_update':
            set_a.difference_update(other_set)
            
    print(sum(set_a))
