# 17.separate the numbers
# Hacker rank link:
https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    length = len(s)
    # The first number can be at most half the length of the string
    for i in range(1, length // 2 + 1):
        first_str = s[:i]
        first_num = int(first_str)
        current_num = first_num
        built_string = first_str
        
        # Build the sequence upwards until its length matches or exceeds the original string
        while len(built_string) < length:
            current_num += 1
            built_string += str(current_num)
            
        # Check if the generated string matches the input string
        if built_string == s:
            print(f"YES {first_num}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
