number_poor_grade = int(input())

flag = False
last_problem = ""
sum_grade = 0
count_problems = 0
current_count_poor = 0

input_line = input()

while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())

    if current_grade <= 4:
        current_count_poor = current_count_poor + 1
    if current_count_poor >= number_poor_grade:
        flag = True
        break

    count_problems = count_problems + 1
    sum_grade = sum_grade + current_grade
    last_problem = problem_name

    input_line = input()

if flag:
    print(f"You need a break, {current_count_poor} poor grades.")
else:
    avg_grade = sum_grade / count_problems
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {last_problem}")
