# 14.Finding the percentage
# Hacker rank Link:
https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    # Read each student's name and marks, and store them in a dictionary
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    # Get the marks list for the queried student
    marks = student_marks[query_name]
    
    # Calculate the average score
    average = sum(marks) / len(marks)
    
    # Print the average formatted to 2 decimal places[cite: 14]
    print(f"{average:.2f}")
