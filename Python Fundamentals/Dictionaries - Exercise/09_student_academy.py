n = int(input())
students_by_grade = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students_by_grade:
        students_by_grade[name] = []
    students_by_grade[name].append(grade)

for name, grade in students_by_grade.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f'{name} -> {average_grade:.2f}')
