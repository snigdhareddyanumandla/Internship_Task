# 3.Mutations
# hacker rank link:
https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    # Convert the string to a list since strings are immutable in Python
    l = list(string)
    # Change the character at the given position
    l[position] = character
    # Join the list back into a string and return it
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
