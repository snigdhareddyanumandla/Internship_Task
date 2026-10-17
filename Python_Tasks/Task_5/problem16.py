# 16.collections-counter
# Hacker rank link:
https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    N = int(input())
    
    # Count the frequency of each available shoe size
    shoe_inventory = Counter(shoe_sizes)
    total_earned = 0
    
    # Process each customer's desired size and price
    for _ in range(N):
        size, price = map(int, input().split())
        # Check if the shoe of the desired size is in stock
        if shoe_inventory[size] > 0:
            total_earned += price
            shoe_inventory[size] -= 1  # Reduce the stock count for that size
            
    # Print the total amount of money earned by Raghu
    print(total_earned)
