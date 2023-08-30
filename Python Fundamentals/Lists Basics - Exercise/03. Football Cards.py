cards = input().split()

a_counter = []
b_counter = []
should_terminate = False
for card in cards:
    if card in a_counter or card in b_counter:
        continue

    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == 'A'
    if is_first_team:
        a_counter.append(card)
    else:
        b_counter.append(card)
    if len(a_counter) > 4 or len(b_counter) > 4:
        should_terminate = True
        break

initial_player_count = 11
final_a = initial_player_count - len(a_counter)
final_b = initial_player_count - len(b_counter)

print(f'Team A - {final_a}; Team B - {final_b}')

if should_terminate:
    print(f'Game was terminated')
