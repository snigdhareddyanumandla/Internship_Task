# 3.Mars Exploration
# Hacker rank link:
https://www.hackerrank.com/challenges/mars-exploration/problem


def marsExploration(s):
    expected = 'SOS' * (len(s) // 3)
    return sum(1 for c1, c2 in zip(s, expected) if c1 != c2)

if __name__ == '__main__':
    s = input()
    result = marsExploration(s)
    print(result)
