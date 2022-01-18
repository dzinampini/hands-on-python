a = {0: 10, 1: 20}

b = int(input("Enter the key number"))

if b in a.keys():
    print(b, "is already in a")
else:
    print(b, "is not in a")
