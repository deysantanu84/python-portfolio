# https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks and student_marks[query_name]:
        print("%.2f" % round(sum(student_marks[query_name])/len(student_marks[query_name]), 2))
