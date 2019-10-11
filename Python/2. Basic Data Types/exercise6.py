# Finding the percentage "https://www.hackerrank.com/challenges/finding-the-percentage/problem"

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    stud_list = student_marks[query_name]
    den = len(stud_list)
    num = sum(stud_list)
    print("{:.2f}".format(num / den))
