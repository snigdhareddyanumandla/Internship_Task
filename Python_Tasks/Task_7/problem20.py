# 20.Super Reduced String
# hacker rank link:
https://www.hackerrank.com/challenges/reduced-string/problem



def superReducedString(s):
    stack = []
    for char in s:
        # If the stack is not empty and the current character matches the top of the stack, pop it (remove adjacent duplicate)
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    # Join the remaining characters or return "Empty String" if the stack is empty
    return "".join(stack) if stack else "Empty String"

if __name__ == '__main__':
    s = input().strip()
    result = superReducedString(s)
    print(result)
