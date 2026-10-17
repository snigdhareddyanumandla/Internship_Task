
# 18.The minion game
# hacker rank link:
https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    # Iterate through each character in the string
    for i in range(length):
        # If the character is a vowel, Kevin gets points for all possible substrings starting at this index
        if string[i] in vowels:
            kevin_score += length - i
        # If it is a consonant, Stuart gets points for all possible substrings starting at this index
        else:
            stuart_score += length - i
            
    # Determine the winner based on the final scores
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
