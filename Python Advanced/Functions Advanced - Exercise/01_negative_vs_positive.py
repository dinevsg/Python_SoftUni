def positive(*args):
    pos_sum = 0
    for x in args:
        if x > 0:
            pos_sum += x
    return pos_sum


def negative(*args):
    neg_sum = 0
    for x in args:
        if x < 0:
            neg_sum += x
    return neg_sum


numbers = [int(x) for x in input().split()]

print(negative(*numbers))
print(positive(*numbers))


if abs(negative(*numbers)) > positive(*numbers):
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
