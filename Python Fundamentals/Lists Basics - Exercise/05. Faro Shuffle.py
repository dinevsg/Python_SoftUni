cards = input().split()
count = int(input())

for shuffle in range(count):
    final_deck = []
    middle_of_deck = len(cards) // 2
    left_part = cards[0:middle_of_deck]
    right_part = cards[middle_of_deck::]
    for card_index in range(len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])

    cards = final_deck
print(cards)
