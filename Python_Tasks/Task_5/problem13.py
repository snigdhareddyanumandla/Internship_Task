# 13.nested lists
# Hacker rabk link:
https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    records = []
    # Read the name and score for each student and store them in a nested list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    # Find all unique scores and sort them in ascending order
    unique_scores = sorted(list(set([score for name, score in records])))
    
    # Identify the second lowest score
    second_lowest = unique_scores[1]
    
    # Collect all student names with that score and sort them alphabetically
    second_lowest_students = sorted([name for name, score in records if score == second_lowest])
    
    # Print each student's name on a new line[cite: 13]
    for student in second_lowest_students:
        print(student)
