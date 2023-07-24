v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

sum_litters = p2 * h + p1 * h

if sum_litters <= v:
    print(f"The pool is {sum_litters / v * 100 }% full."
          f"Pipe 1: {p1 * h / sum_litters * 100:.2f}%."
          f"Pipe 2: {p2 * h / sum_litters * 100:.2f}%.")
elif sum_litters > v:
    print(f"For {h:.2f} hours the pool overflows with {sum_litters - v:.2f} liters.")
