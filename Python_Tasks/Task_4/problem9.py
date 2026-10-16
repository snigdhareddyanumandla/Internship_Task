# 9.mutations
# hacker rank link:
https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    # Slice the string up to the position, add the new character, and slice from position + 1 onwards
    return string[:position] + character + string[position + 1:]
