# pilling up!
# Hacker rank link:
https://www.hackerrank.com/challenges/piling-up/problem




from collections import deque

def solve_piling_up():
    T = int(input())
    for _ in range(T):
        n = int(input())
        blocks = deque(map(int, input().split()))
        
        # Initialize last_block with infinity to accept the first chosen cube
        last_block = float('inf')
        possible = True
        
        while blocks:
            # Always pick the larger of the two ends to maintain valid stacking rules
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()
                
            # Check if the current block can be placed on top of the previous block
            if current <= last_block:
                last_block = current
            else:
                possible = False
                break
                
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve_piling_up()
