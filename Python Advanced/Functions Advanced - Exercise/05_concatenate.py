def concatenate(*args, **kwargs):
    a = "".join(args)
    for k, v in kwargs.items():
        a = a.replace(k, v)
    return a



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
