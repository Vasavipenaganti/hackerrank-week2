if __name__ == '__main__':
    students = []
    for _ in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])
    scores = sorted(set([score for name, score in students]))
    second_lowest_score = scores[1]
    second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])
    for student in second_lowest_students:
        print(student)
