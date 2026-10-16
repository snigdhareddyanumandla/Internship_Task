# 16.nested list
# hacker rank link:
https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    # Extract unique grades and find the second lowest grade
    grades = sorted(list(set(score for name, score in records)))
    second_lowest = grades[1]
    
    # Collect all student names with the second lowest grade and sort them alphabetically
    result_names = sorted([name for name, score in records if score == second_lowest])
    
    # Print each name on a new line
    for name in result_names:
        print(name)
