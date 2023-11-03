def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantity in sorted_cheeses:
        result += cheese + "\n"
        reversed_quantities = sorted(quantity, reverse=True)
        result += "\n".join(str(el) for el in reversed_quantities) + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)