def grocery_store(**kwargs):
    result = []
    sorted_receipt = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for name, quantity in sorted_receipt:
        result.append(f"{name}: {quantity}")

    return "\n".join(result)

# pasta: 12
# eggs: 12
# bread: 5


print(grocery_store(
    bread=5,
    pasta=12,
    eggss=12,
    )
)
