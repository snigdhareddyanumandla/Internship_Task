#2.string-split and join
# Hacker rank link:
https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # Split the string on a space delimiter and join using a hyphen
    result = "-".join(line.split(" "))
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
