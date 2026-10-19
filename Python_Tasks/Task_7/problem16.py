# 16.caesar cipher
# Hacker rank link:
https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(s, k):
    encrypted = []
    for char in s:
        if char.isupper():
            # Shift uppercase letters while preserving case and wrapping around the alphabet
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted.append(shifted)
        elif char.islower():
            # Shift lowercase letters while preserving case and wrapping around the alphabet
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted.append(shifted)
        else:
            # Leave symbols, spaces, and numbers unencrypted
            encrypted.append(char)
            
    return "".join(encrypted)

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())
    result = caesarCipher(s, k)
    print(result)
