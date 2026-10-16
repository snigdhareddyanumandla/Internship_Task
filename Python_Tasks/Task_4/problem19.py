# 19.collections-counters
# hacker rank link:
https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    N = int(input())
    
    # Count the frequency of each shoe size available in the shop
    inventory = Counter(shoe_sizes)
    earnings = 0
    
    # Process each customer's request
    for _ in range(N):
        size, price = map(int, input().split())
        # If the requested size is in stock, sell it and add the price to earnings
        if inventory[size] > 0:
            earnings += price
            inventory[size] -= 1
            
    # Print the total money earned by Raghu
    print(earnings)
