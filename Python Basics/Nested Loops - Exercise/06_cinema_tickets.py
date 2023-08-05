students_counter = 0
kids_counter = 0
standard_counter = 0
total_tickets_counter = 0

command = input()

while command != "Finish":
    total_spaces = int(input())
    movie_name = command
    sold_movie_tickets = 0
    free_spaces = total_spaces

    while free_spaces > 0:
        ticket_type = input()

        if ticket_type == "End":
            break
        if ticket_type == "student":
            students_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        else:
            kids_counter += 1

        total_tickets_counter += 1
        sold_movie_tickets += 1
        free_spaces -= 1

    print(f"{command} - {sold_movie_tickets / total_spaces * 100:.2f}% full.")

    command = input()

print(f"Total tickets: {total_tickets_counter}")
print(f"{(students_counter / total_tickets_counter * 100):.2f}% student tickets.")
print(f"{standard_counter / total_tickets_counter * 100:.2f}% standard tickets.")
print(f"{kids_counter / total_tickets_counter * 100:.2f}% kids tickets.")
