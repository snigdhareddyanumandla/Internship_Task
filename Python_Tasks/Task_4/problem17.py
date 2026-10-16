# 17.finding the percentage
# hacker rank link:
https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        line = input().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        student_marks[name] = scores
        
    query_name = input()
    
    # Retrieve the marks list for the queried student and calculate the average
    query_scores = student_marks[query_name]
    average_score = sum(query_scores) / len(query_scores)
    
    # Print the average correct to 2 decimal places
    print(f"{average_score:.2f}")
