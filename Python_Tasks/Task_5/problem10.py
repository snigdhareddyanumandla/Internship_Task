# 10.SwAp cAse
# hacker rank link:
https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    # The swapcase() method converts all lowercase letters to uppercase and vice versa
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
