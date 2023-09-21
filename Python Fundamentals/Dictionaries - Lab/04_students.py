text = input()
courses = {}

while ":" in text:
    name, uid, course = text.split(":")
    if course not in courses:
        courses[course] = {uid: name}
    else:
        courses[course][uid] = name

    text = input()
course = " ".join(text.split("_"))
students = courses[course]
for uid, name in students.items():
    print(f"{name} - {uid}")





