budget = float(input())
season = input()

destination = ""
type_vac = ""

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        budget = budget * 0.3
        type_vac = "Camp"
    elif season == "winter":
        budget = budget * 0.70
        type_vac = "Hotel"

    print(f"Somewhere in {destination}")
    print(f"{type_vac} - {budget:.2f}")

if 1000 >= budget > 100:
    destination = "Balkans"

    if season == "summer":
        budget = budget * 0.40
        type_vac = "Camp"
    elif season == "winter":
        budget = budget * 0.80
        type_vac = "Hotel"

    print(f"Somewhere in {destination}")
    print(f"{type_vac} - {budget:.2f}")

if budget > 1000:
    destination = "Europe"

    if destination == "Europe":
        budget = budget * 0.90
        type_vac = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{type_vac} - {budget:.2f}")
