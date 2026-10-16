# 18.list
# hacker rank list:
https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            eval(f"L.{cmd}({','.join(args)})")
        else:
            print(L)
