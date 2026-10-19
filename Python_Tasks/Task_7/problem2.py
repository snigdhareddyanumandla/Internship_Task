# 2.The Captain's Room
# Hacker rank link:
https://www.hackerrank.com/challenges/py-the-captains-room/problem


if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    
    # Using sets to find the unique room numbers and the Captain's room
    unique_rooms = set(rooms)
    
    # Mathematical set logic: (sum of unique rooms * K) - (sum of all rooms) = (K - 1) * Captain's room
    captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)
    print(captain_room)
