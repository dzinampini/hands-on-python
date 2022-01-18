def swap(a, b):
    a = a - b
    b = a + b
    a = a - b

    if a < 0:
        return -(a), b
    elif b < 0:
        return a, -(b)


print(swap(20, 15))
